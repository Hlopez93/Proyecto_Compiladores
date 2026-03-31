class TablaSimbolos:

    def __init__(self):
        self.scopes = [{}]  # scope global

    # ---------------- SCOPES ----------------
    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()
        else:
            raise Exception("Error: No se puede eliminar el scope global")

    # ---------------- DECLARAR ----------------
    def declarar(self, nombre, tipo, valor=None):
        scope_actual = self.scopes[-1]

        if nombre in scope_actual:
            raise Exception(f"Error: Variable '{nombre}' ya declarada en este ámbito")

        scope_actual[nombre] = {
            "tipo": tipo,
            "valor": valor
        }

    # ---------------- ASIGNAR ----------------
    def asignar(self, nombre, valor):
        for scope in reversed(self.scopes):
            if nombre in scope:
                scope[nombre]["valor"] = valor
                return

        raise Exception(f"Error: Variable '{nombre}' no declarada")

    # ---------------- OBTENER ----------------
    def obtener(self, nombre):
        for scope in reversed(self.scopes):
            if nombre in scope:
                return scope[nombre]

        raise Exception(f"Error: Variable '{nombre}' no declarada")