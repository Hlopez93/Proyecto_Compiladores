from gramatica_v3Visitor import gramatica_v3Visitor
from gramatica_v3Parser import gramatica_v3Parser
from tablaSimbolos import TablaSimbolos

class SemanticVisitor(gramatica_v3Visitor):

    def __init__(self):
        self.tabla = TablaSimbolos()
        self.current_function = None
        self.loop_depth = 0

    def visitRoot(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitBlock(self, ctx):
        self.tabla.push_scope()
        for stmt in ctx.statement():
            self.visit(stmt)
        self.tabla.pop_scope()

    def visitDeclaration(self, ctx):
        stmt = ctx.declarationStatement()

        nombre = stmt.VAR().getText()
        tipo = stmt.tipo().getText()

        if stmt.expr():
            tipo_expr = self.visit(stmt.expr())
            if tipo_expr != tipo:
                raise Exception("Error semántico: tipos incompatibles en declaración")

        self.tabla.declarar(nombre, tipo)

    def visitDeclarationStatement(self, ctx):
        nombre = ctx.VAR().getText()
        tipo = ctx.tipo().getText()

        es_array = "[]" in tipo

        if ctx.expr():
            tipo_expr = self.visit(ctx.expr())
            if tipo_expr != tipo:
                raise Exception("Error semántico: tipos incompatibles en declaración")

        if ctx.arrayLiteral():
            if not es_array:
                raise Exception("Error: asignación de array a variable no array")

            # validar elementos del array
            tipos = [self.visit(e) for e in ctx.arrayLiteral().expr()]
            base = tipo.replace("[]", "")

            for t in tipos:
                if t != base:
                    raise Exception("Error: tipos incompatibles dentro del array")

        self.tabla.declarar(nombre, tipo)

    def visitAssignment(self, ctx):
        stmt = ctx.assignmentStatement()

        nombre = stmt.VAR().getText()
        var = self.tabla.obtener(nombre)

        tipo_expr = self.visit(stmt.expr())

        if var["tipo"] != tipo_expr:
            raise Exception("Error semántico: tipos incompatibles en asignación")
        
    def visitAssignmentStatement(self, ctx):
        nombre = ctx.VAR().getText()
        var = self.tabla.obtener(nombre)

        tipo_expr = self.visit(ctx.expr())

        if var["tipo"] != tipo_expr:
            raise Exception("Error semántico: tipos incompatibles en asignación")
        
    def visitArrayLiteral(self, ctx):
        # devuelve tipo del array: int[], float[], etc.
        tipos = [self.visit(e) for e in ctx.expr()]
        base = tipos[0]

        for t in tipos:
            if t != base:
                raise Exception("Error: array con tipos mixtos")

        return base + "[]"

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

    def visitIfStatement(self, ctx):
        if self.visit(ctx.condition()) != "bool":
            raise Exception("Error: condición de if debe ser bool")

        self.visit(ctx.block(0))
        if ctx.ELSE():
            self.visit(ctx.block(1))

    def visitWhileStatement(self, ctx):
        if self.visit(ctx.condition()) != "bool":
            raise Exception("Error: condición de while debe ser bool")

        self.loop_depth += 1
        self.visit(ctx.block())
        self.loop_depth -= 1

    def visitForStatement(self, ctx):
        self.tabla.push_scope()
        self.loop_depth += 1

        if ctx.forInit():
            if ctx.forInit().declarationStatement():
                self.visit(ctx.forInit().declarationStatement())
            else:
                self.visit(ctx.forInit().assignmentStatement())

        if ctx.condition():
            if self.visit(ctx.condition()) != "bool":
                raise Exception("Error: condición de for debe ser bool")

        self.visit(ctx.block())

        if ctx.forUpdate():
            self.visit(ctx.forUpdate().assignmentStatement())

        self.loop_depth -= 1
        self.tabla.pop_scope()

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

    def visitExpr(self, ctx):
        if ctx.NUM(): return "int"
        if ctx.FLOAT(): return "float"
        if ctx.STRING(): return "string"
        if ctx.TRUE() or ctx.FALSE(): return "bool"

        # acceso array
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '[':
            nombre = ctx.getChild(0).getText()
            tipo = self.tabla.obtener(nombre)["tipo"]

            if "[]" not in tipo:
                raise Exception("Error: variable no es un array")

            index_type = self.visit(ctx.expr(0))
            if index_type != "int":
                raise Exception("Error: índice de array debe ser int")

            return tipo.replace("[]", "")

        if ctx.VAR():
            return self.tabla.obtener(ctx.VAR().getText())["tipo"]

        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        if len(ctx.expr()) == 2:
            t1 = self.visit(ctx.expr(0))
            t2 = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()

            if op == '+':
                if t1 == "string" and t2 == "string":
                    return "string"

            if t1 != t2:
                raise Exception("Error: operación entre tipos incompatibles")

            if op == '%':
                if t1 != "int":
                    raise Exception("Error: % solo permitido en enteros")
                return "int"

            return t1
        
        def visitBreakStmt(self, ctx):
            if self.loop_depth == 0:
                raise Exception("Error: break fuera de ciclo")

        def visitContinueStmt(self, ctx):
            if self.loop_depth == 0:
                raise Exception("Error: continue fuera de ciclo")
            
        def visitImportStmt(self, ctx):
            # validación mínima
            return None

        if ctx.expr():
            return self.visit(ctx.expr(0))