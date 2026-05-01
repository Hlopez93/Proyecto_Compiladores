from compiler.gramatica_v3Visitor import gramatica_v3Visitor
from compiler.semantic.tablaSimbolos import TablaSimbolos

class SemanticVisitor(gramatica_v3Visitor):

    def __init__(self):
        self.tabla = TablaSimbolos()
        self.current_function = None
        self.in_loop = 0  # control para break/continue

    # ROOT
    def visitRoot(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # BLOCK
    def visitBlock(self, ctx):
        self.tabla.push_scope()
        for stmt in ctx.statement():
            self.visit(stmt)
        self.tabla.pop_scope()

    # DECLARACIÓN
    def visitDeclaration(self, ctx):
        self.visit(ctx.declarationStatement())

    def visitDeclarationStatement(self, ctx):
        nombre = ctx.VAR().getText()
        tipo = ctx.tipo().getText()
        decl = ctx.DECL().getText()  # var | let | const

        valor_tipo = None

        if ctx.arrayLiteral():
            valor_tipo = self.visit(ctx.arrayLiteral())

        elif ctx.expr():
            valor_tipo = self.visit(ctx.expr())

        # Validación de tipos
        if valor_tipo:
            if valor_tipo != tipo:
                raise Exception(f"Error semántico: tipos incompatibles en declaración '{nombre}'")

        self.tabla.declarar(
            nombre,
            tipo,
            mutable=(decl != "const")
        )

    # ARRAY
    def visitArrayLiteral(self, ctx):
        tipos = [self.visit(e) for e in ctx.expr()]

        if len(set(tipos)) != 1:
            raise Exception("Error semántico: array con tipos mixtos")

        return tipos[0] + "[]"

    # ASIGNACIÓN
    def visitAssignment(self, ctx):
        self.visit(ctx.assignmentStatement())

    def visitAssignmentStatement(self, ctx):
        nombre = ctx.VAR().getText()
        var = self.tabla.obtener(nombre)

        if not var.get("mutable", True):
            raise Exception(f"Error: '{nombre}' es const y no puede modificarse")

        tipo_expr = self.visit(ctx.expr())

        if tipo_expr != var["tipo"]:
            raise Exception("Error semántico: tipos incompatibles en asignación")

    # FUNCIONES
    def visitFunctionDecl(self, ctx):
        nombre = ctx.VAR().getText()
        tipo_retorno = ctx.tipo().getText()

        parametros = []
        if ctx.paramList():
            for p in ctx.paramList().param():
                parametros.append((p.VAR().getText(), p.tipo().getText()))

        self.tabla.declarar_funcion(nombre, tipo_retorno, parametros, ctx)

        prev = self.current_function
        self.current_function = tipo_retorno

        self.tabla.push_scope()

        for n, t in parametros:
            self.tabla.declarar(n, t)

        self.visit(ctx.block())

        self.tabla.pop_scope()
        self.current_function = prev

    def visitReturnStmt(self, ctx):
        if self.current_function is None:
            raise Exception("Error semántico: return fuera de función")

        if ctx.expr():
            tipo_expr = self.visit(ctx.expr())
            if tipo_expr != self.current_function:
                raise Exception("Error semántico: tipo de retorno incorrecto")
        else:
            if self.current_function != "void":
                raise Exception("Error semántico: return vacío en función no void")

    def visitFunctionCall(self, ctx):
        nombre = ctx.VAR().getText()
        func = self.tabla.obtener_funcion(nombre)

        args = []
        if ctx.argList():
            args = [self.visit(e) for e in ctx.argList().expr()]

        if len(args) != len(func["parametros"]):
            raise Exception("Error: número incorrecto de argumentos")

        for i, (n, t) in enumerate(func["parametros"]):
            if args[i] != t:
                raise Exception("Error: tipo de argumento incorrecto")

        return func["retorno"]

    # CONTROL DE FLUJO
    def visitIfStatement(self, ctx):
        if self.visit(ctx.condition()) != "bool":
            raise Exception("Error: condición de if debe ser bool")

        self.visit(ctx.block(0))
        if ctx.ELSE():
            self.visit(ctx.block(1))

    def visitWhileStatement(self, ctx):
        if self.visit(ctx.condition()) != "bool":
            raise Exception("Error: condición de while debe ser bool")

        self.in_loop += 1
        self.visit(ctx.block())
        self.in_loop -= 1

    def visitForStatement(self, ctx):
        self.tabla.push_scope()

        if ctx.forInit():
            if ctx.forInit().declarationStatement():
                self.visit(ctx.forInit().declarationStatement())
            else:
                self.visit(ctx.forInit().assignmentStatement())

        if ctx.condition():
            if self.visit(ctx.condition()) != "bool":
                raise Exception("Error: condición de for debe ser bool")

        self.in_loop += 1

        self.tabla.push_scope()
        for stmt in ctx.block().statement():
            self.visit(stmt)
        self.tabla.pop_scope()

        if ctx.forUpdate():
            self.visit(ctx.forUpdate().assignmentStatement())

        self.in_loop -= 1

        self.tabla.pop_scope()

    def visitBreakStmt(self, ctx):
        if self.in_loop == 0:
            raise Exception("Error: break fuera de ciclo")

    def visitContinueStmt(self, ctx):
        if self.in_loop == 0:
            raise Exception("Error: continue fuera de ciclo")

    # IMPORT
    def visitImportStmt(self, ctx):
        # No se valida aún (fase futura)
        return

    # CONDICIONES
    def visitCondition(self, ctx):

        if ctx.AND() or ctx.OR():
            if self.visit(ctx.condition(0)) != "bool" or self.visit(ctx.condition(1)) != "bool":
                raise Exception("Error: operadores lógicos requieren booleanos")
            return "bool"

        if ctx.NOT():
            if self.visit(ctx.condition(0)) != "bool":
                raise Exception("Error: NOT requiere booleano")
            return "bool"

        if ctx.relop():
            if self.visit(ctx.expr(0)) != self.visit(ctx.expr(1)):
                raise Exception("Error: comparación inválida")
            return "bool"

        if ctx.TRUE() or ctx.FALSE():
            return "bool"

        if ctx.condition():
            return self.visit(ctx.condition(0))

    # EXPRESIONES
    def visitExpr(self, ctx):

        if ctx.NUM():
            return "int"

        if ctx.FLOAT():
            return "float"

        if ctx.STRING():
            return "string"

        if ctx.TRUE() or ctx.FALSE():
            return "bool"

        # ARRAY ACCESS
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '[':
            nombre = ctx.VAR().getText()
            var = self.tabla.obtener(nombre)

            if "[]" not in var["tipo"]:
                raise Exception("Error: variable no es un array")

            tipo_index = self.visit(ctx.expr(0))
            if tipo_index != "int":
                raise Exception("Error: índice debe ser int")

            return var["tipo"].replace("[]", "")

        if ctx.VAR():
            return self.tabla.obtener(ctx.VAR().getText())["tipo"]

        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        if len(ctx.expr()) == 2:
            t1 = self.visit(ctx.expr(0))
            t2 = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()

            if t1 != t2:
                raise Exception("Error: operación entre tipos incompatibles")

            if op == '%':
                if t1 != "int":
                    raise Exception("Error: % solo válido para enteros")
                return "int"

            return t1

        if ctx.expr():
            return self.visit(ctx.expr(0))