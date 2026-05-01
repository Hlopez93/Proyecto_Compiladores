class TablaSimbolos:

    def __init__(self):
        self.scopes = [{}]
        self.funciones = {}

    # SCOPES
    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        self.scopes.pop()

    def scope_actual(self):
        return self.scopes[-1]

    # VARIABLES
    def declarar(self, nombre, tipo, valor=None, mutable=True):

        scope = self.scope_actual()

        if nombre in scope:
            raise Exception(f"Error semántico: Variable '{nombre}' ya declarada en este scope")

        scope[nombre] = {
            "tipo": tipo,
            "valor": valor,
            "mutable": mutable
        }

    def obtener(self, nombre):

        for scope in reversed(self.scopes):
            if nombre in scope:
                return scope[nombre]

        raise Exception(f"Error semántico: Variable '{nombre}' no declarada")

    def asignar(self, nombre, valor):

        for scope in reversed(self.scopes):
            if nombre in scope:

                if not scope[nombre]["mutable"]:
                    raise Exception(f"Error semántico: Variable '{nombre}' es constante (const)")

                scope[nombre]["valor"] = valor
                return

        raise Exception(f"Error semántico: Variable '{nombre}' no declarada")

    # FUNCIONES
    def declarar_funcion(self, nombre, tipo_retorno, parametros, ctx):

        if nombre in self.funciones:
            raise Exception(f"Error semántico: Función '{nombre}' ya declarada")

        self.funciones[nombre] = {
            "retorno": tipo_retorno,
            "parametros": parametros,
            "ctx": ctx
        }

    def obtener_funcion(self, nombre):

        if nombre not in self.funciones:
            raise Exception(f"Error semántico: Función '{nombre}' no declarada")

        return self.funciones[nombre]