from llvmlite import ir
from gramatica_v3Visitor import gramatica_v3Visitor


class IRGenerator(gramatica_v3Visitor):

    def __init__(self):
        self.module = ir.Module(name="module")

        self.loop_stack = []

        self.builder = None
        self.func = None

        self.variables = {}
        self.functions = {}

        # printf
        printf_type = ir.FunctionType(
            ir.IntType(32),
            [ir.IntType(8).as_pointer()],
            var_arg=True
        )
        self.printf = ir.Function(self.module, printf_type, name="printf")

    # ========================
    # ROOT
    # ========================
    def visitRoot(self, ctx):

        func_type = ir.FunctionType(ir.IntType(32), [])
        self.func = ir.Function(self.module, func_type, name="main")

        block = self.func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        for stmt in ctx.statement():
            self.visit(stmt)

        self.builder.ret(ir.Constant(ir.IntType(32), 0))

    # ========================
    # DECLARACIÓN
    # ========================
    def visitDeclaration(self, ctx):
        stmt = ctx.declarationStatement()
        nombre = stmt.VAR().getText()
        tipo = stmt.tipo().getText()

        llvm_type = self.get_llvm_type(tipo)

        ptr = self.builder.alloca(llvm_type, name=nombre)
        self.variables[nombre] = ptr

        if stmt.expr():
            val = self.visit(stmt.expr())
            self.builder.store(val, ptr)

    def visitDeclarationStatement(self, ctx):
        nombre = ctx.VAR().getText()
        tipo = ctx.tipo().getText()

        llvm_type = self.get_llvm_type(tipo)

        ptr = self.builder.alloca(llvm_type, name=nombre)
        self.variables[nombre] = ptr

        if ctx.expr():
            val = self.visit(ctx.expr())
            self.builder.store(val, ptr)

    # ========================
    # ASIGNACIÓN
    # ========================
    def visitAssignmentStatement(self, ctx):
        nombre = ctx.VAR().getText()

        if nombre not in self.variables:
            raise Exception(f"Variable '{nombre}' no definida en IR")

        val = self.visit(ctx.expr())
        self.builder.store(val, self.variables[nombre])

    # ========================
    # EXPRESIONES
    # ========================
    def visitExpr(self, ctx):

        # INT
        if ctx.NUM():
            return ir.Constant(ir.IntType(32), int(ctx.NUM().getText()))

        # FLOAT
        if ctx.FLOAT():
            return ir.Constant(ir.DoubleType(), float(ctx.FLOAT().getText()))

        # STRING
        if ctx.STRING():
            text = ctx.STRING().getText()[1:-1]
            global_str = self.create_string(text, "str_lit")
            return self.builder.bitcast(global_str, ir.IntType(8).as_pointer())

        # BOOL
        if ctx.TRUE():
            return ir.Constant(ir.IntType(1), 1)

        if ctx.FALSE():
            return ir.Constant(ir.IntType(1), 0)

        # VARIABLE
        if ctx.VAR():
            name = ctx.VAR().getText()
            if name not in self.variables:
                raise Exception(f"Variable '{name}' no definida en IR")

            ptr = self.variables[name]
            return self.builder.load(ptr)

        # FUNCIÓN
        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        # OPERACIONES
        if len(ctx.expr()) == 2:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()

            # FLOAT
            if isinstance(left.type, ir.DoubleType):
                if op == '+': return self.builder.fadd(left, right)
                if op == '-': return self.builder.fsub(left, right)
                if op == '*': return self.builder.fmul(left, right)
                if op == '/': return self.builder.fdiv(left, right)

            # INT
            else:
                if op == '+': return self.builder.add(left, right)
                if op == '-': return self.builder.sub(left, right)
                if op == '*': return self.builder.mul(left, right)
                if op == '/': return self.builder.sdiv(left, right)
                if op == '%': return self.builder.srem(left, right)

        if ctx.expr():
            return self.visit(ctx.expr(0))

    # ========================
    # TIPOS
    # ========================
    def get_llvm_type(self, tipo):
        if tipo == "int":
            return ir.IntType(32)
        if tipo == "float":
            return ir.DoubleType()
        if tipo == "bool":
            return ir.IntType(1)
        if tipo == "string":
            return ir.IntType(8).as_pointer()
        return ir.VoidType()

    # ========================
    # CONDITION
    # ========================
    def visitCondition(self, ctx):

        if ctx.TRUE():
            return ir.Constant(ir.IntType(1), 1)

        if ctx.FALSE():
            return ir.Constant(ir.IntType(1), 0)

        if ctx.AND():
            return self.builder.and_(
                self.visit(ctx.condition(0)),
                self.visit(ctx.condition(1))
            )

        if ctx.OR():
            return self.builder.or_(
                self.visit(ctx.condition(0)),
                self.visit(ctx.condition(1))
            )

        if ctx.NOT():
            val = self.visit(ctx.condition(0))
            return self.builder.icmp_signed('==', val, ir.Constant(val.type, 0))

        if ctx.relop():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.relop().getText()

            return self.builder.icmp_signed(op, left, right)

    # ========================
    # IF
    # ========================
    def visitIfStatement(self, ctx):

        cond = self.visit(ctx.condition())

        then_block = self.func.append_basic_block('then')
        else_block = self.func.append_basic_block('else') if ctx.ELSE() else None
        merge_block = self.func.append_basic_block('ifend')

        if else_block:
            self.builder.cbranch(cond, then_block, else_block)
        else:
            self.builder.cbranch(cond, then_block, merge_block)

        # THEN
        self.builder.position_at_start(then_block)
        self.visit(ctx.block(0))
        if not self.builder.block.is_terminated:
            self.builder.branch(merge_block)

        # ELSE
        if else_block:
            self.builder.position_at_start(else_block)
            self.visit(ctx.block(1))
            if not self.builder.block.is_terminated:
                self.builder.branch(merge_block)

        self.builder.position_at_start(merge_block)

    # ========================
    # WHILE
    # ========================
    def visitWhileStatement(self, ctx):

        cond_block = self.func.append_basic_block('while_cond')
        body_block = self.func.append_basic_block('while_body')
        end_block = self.func.append_basic_block('while_end')

        self.builder.branch(cond_block)

        # COND
        self.builder.position_at_start(cond_block)
        cond = self.visit(ctx.condition())
        self.builder.cbranch(cond, body_block, end_block)

        # BODY
        self.builder.position_at_start(body_block)

        self.loop_stack.append({
            "continue": cond_block,
            "break": end_block
        })

        self.visit(ctx.block())
        self.loop_stack.pop()

        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)

        # END
        self.builder.position_at_start(end_block)

    # ========================
    # BREAK / CONTINUE
    # ========================
    def visitBreakStmt(self, ctx):
        if not self.loop_stack:
            raise Exception("break fuera de ciclo")

        target = self.loop_stack[-1]["break"]
        self.builder.branch(target)

        new_block = self.func.append_basic_block(f'after_break_{id(ctx)}')
        self.builder.position_at_start(new_block)

    def visitContinueStmt(self, ctx):
        if not self.loop_stack:
            raise Exception("continue fuera de ciclo")

        target = self.loop_stack[-1]["continue"]
        self.builder.branch(target)

        new_block = self.func.append_basic_block(f'after_continue_{id(ctx)}')
        self.builder.position_at_start(new_block)

    # ========================
    # FUNCIONES
    # ========================
    def visitFunctionDecl(self, ctx):

        nombre = ctx.VAR().getText()
        tipo_retorno = ctx.tipo().getText()

        ret_type = self.get_llvm_type(tipo_retorno)

        param_types = []
        param_names = []

        if ctx.paramList():
            for p in ctx.paramList().param():
                param_types.append(self.get_llvm_type(p.tipo().getText()))
                param_names.append(p.VAR().getText())

        func_type = ir.FunctionType(ret_type, param_types)
        func = ir.Function(self.module, func_type, name=nombre)

        self.functions[nombre] = func

        prev_builder = self.builder
        prev_func = self.func
        prev_vars = self.variables

        self.func = func
        self.variables = {}

        block = func.append_basic_block('entry')
        self.builder = ir.IRBuilder(block)

        for i, arg in enumerate(func.args):
            arg.name = param_names[i]
            ptr = self.builder.alloca(arg.type, name=arg.name)
            self.builder.store(arg, ptr)
            self.variables[arg.name] = ptr

        self.visit(ctx.block())

        if not self.builder.block.is_terminated:
            if isinstance(ret_type, ir.VoidType):
                self.builder.ret_void()
            else:
                self.builder.ret(ir.Constant(ret_type, 0))

        self.builder = prev_builder
        self.func = prev_func
        self.variables = prev_vars

    def visitReturnStmt(self, ctx):
        if ctx.expr():
            val = self.visit(ctx.expr())
            self.builder.ret(val)
        else:
            self.builder.ret_void()

    def visitFunctionCall(self, ctx):

        nombre = ctx.VAR().getText()
        func = self.functions[nombre]

        args = []
        if ctx.argList():
            args = [self.visit(e) for e in ctx.argList().expr()]

        return self.builder.call(func, args)

    # ========================
    # STRINGS
    # ========================
    def create_string(self, text, name="str"):
        unique_name = f"{name}_{len(self.module.globals)}"

        text_bytes = bytearray(text.encode("utf8")) + b'\00'
        string_type = ir.ArrayType(ir.IntType(8), len(text_bytes))

        global_str = ir.GlobalVariable(self.module, string_type, name=unique_name)
        global_str.global_constant = True
        global_str.initializer = ir.Constant(string_type, text_bytes)

        return global_str

    # ========================
    # PRINT
    # ========================
    def visitPrintStmt(self, ctx):

        value = self.visit(ctx.expr())

        # INT
        if isinstance(value.type, ir.IntType) and value.type.width == 32:
            fmt = self.create_string("%d\n", "fmt_int")
            fmt_ptr = self.builder.bitcast(fmt, ir.IntType(8).as_pointer())
            self.builder.call(self.printf, [fmt_ptr, value])

        # BOOL
        elif isinstance(value.type, ir.IntType) and value.type.width == 1:
            fmt = self.create_string("%d\n", "fmt_bool")
            fmt_ptr = self.builder.bitcast(fmt, ir.IntType(8).as_pointer())
            val32 = self.builder.zext(value, ir.IntType(32))
            self.builder.call(self.printf, [fmt_ptr, val32])

        # FLOAT
        elif isinstance(value.type, ir.DoubleType):
            fmt = self.create_string("%f\n", "fmt_float")
            fmt_ptr = self.builder.bitcast(fmt, ir.IntType(8).as_pointer())
            self.builder.call(self.printf, [fmt_ptr, value])

        # STRING
        elif isinstance(value.type, ir.PointerType):
            fmt = self.create_string("%s\n", "fmt_str")
            fmt_ptr = self.builder.bitcast(fmt, ir.IntType(8).as_pointer())
            self.builder.call(self.printf, [fmt_ptr, value])

    # ========================
    # IMPORT (IGNORADO)
    # ========================
    def visitImportStmt(self, ctx):
        return