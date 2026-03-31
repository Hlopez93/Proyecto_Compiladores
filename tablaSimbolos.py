class TablaSimbolos:

    def __init__(self):
        self.scopes = [{}]

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()
        else:
            raise Exception("Error: No se puede eliminar el scope global")

    def declarar(self, nombre, tipo, valor=None):
        scope_actual = self.scopes[-1]

        if nombre in scope_actual:
            raise Exception(f"Error: Variable '{nombre}' ya declarada")

        scope_actual[nombre] = {
            "tipo": tipo,
            "valor": valor
        }

    def asignar(self, nombre, valor):
        for scope in reversed(self.scopes):
            if nombre in scope:
                scope[nombre]["valor"] = valor
                return
        raise Exception(f"Error: Variable '{nombre}' no declarada")

    def obtener(self, nombre):
        for scope in reversed(self.scopes):
            if nombre in scope:
                return scope[nombre]
        raise Exception(f"Error: Variable '{nombre}' no declarada")

    def declarar_funcion(self, nombre, tipo_retorno, parametros, ctx):
        if nombre in self.scopes[0]:
            raise Exception(f"Error: función '{nombre}' ya declarada")

        self.scopes[0][nombre] = {
            "tipo": "function",
            "retorno": tipo_retorno,
            "parametros": parametros,
            "ctx": ctx
        }

    def obtener_funcion(self, nombre):
        if nombre in self.scopes[0]:
            return self.scopes[0][nombre]
        raise Exception(f"Error: función '{nombre}' no declarada")