from graphviz import Digraph


class ExpresionRegular:
    def __init__(self, expresion):
        self.expresion = expresion
        self.estados = set()
        self.transiciones = {}
        self.estado_final = None

    def get_estados(self):
        return self.estados

    def get_transiciones(self):
        return self.transiciones

    def get_estado_final(self):
        return self.estado_final

    def transformar_a_automata(self):
        # Lógica para transformar la expresión regular en un autómata
        self._procesar_expresion()

    def obtener_cantidad_estados(self):
        return len(self.estados)

    def obtener_cantidad_transiciones(self):
        count = 0
        for transiciones in self.transiciones.values():
            count += len(transiciones)
        return count

    def obtener_alfabeto(self):
        """Returns the alphabet (set of unique symbols) used in the expression."""
        alfabeto = set()
        for estados, transiciones in self.transiciones.items():
            for simbolo, _ in transiciones.items():
                alfabeto.add(simbolo)
        return alfabeto

    def imprimir_informacion(self):
        """Prints information about the regular expression."""
        print("Expresión regular:", self.expresion)
        print("Cantidad de estados:", self.obtener_cantidad_estados())
        print("Cantidad de transiciones:", self.obtener_cantidad_transiciones())
        print("Alfabeto:", self.obtener_alfabeto())
        print("Estados:", self.get_estados())
        print("Transiciones:", self.get_transiciones())
        print("Estado final:", self.get_estado_final())

    def _procesar_expresion(self):
        stack = []
        for char in self.expresion:
            if char == '(':
                stack.append('(')
            elif char == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
            elif char == '|':
                self._procesar_union(stack)
            elif char == '*':
                self._procesar_cerradura(stack)
            elif char == '.':
                self._procesar_concatenacion(stack)
            else:
                self._procesar_simbolo(char, stack)

        self.estado_final = stack[0]
        return self

    def _procesar_union(self, stack):
        if len(stack) < 2:
            raise ValueError("Expresión regular no válida")
        estado1 = stack.pop(-2)
        estado2 = stack.pop()
        nuevo_estado = self._obtener_nuevo_estado()
        self._agregar_transicion(nuevo_estado, 'ε', estado1)
        self._agregar_transicion(nuevo_estado, 'ε', estado2)
        stack.append(nuevo_estado)

    def _procesar_cerradura(self, stack):
        if len(stack) < 1:
            raise ValueError("Expresión regular no válida")
        estado = stack.pop()
        nuevo_estado = self._obtener_nuevo_estado()
        self._agregar_transicion(nuevo_estado, 'ε', estado)
        self._agregar_transicion(estado, 'ε', nuevo_estado)
        stack.append(nuevo_estado)

    def _procesar_concatenacion(self, stack):
        if len(stack) < 2:
            raise ValueError("Expresión regular no válida")
        estado2 = stack.pop()
        estado1 = stack.pop()
        self._agregar_transicion(estado1, 'ε', estado2)
        stack.append(estado1)

    def _procesar_simbolo(self, char, stack):
        if char in ["*", "(", ")", "|", "."]:
            # Si el caracter es un operador, se agrega a la pila
            stack.append(char)
        else:
            # Si el caracter es un simbolo normal, se crea un nuevo estado
            nuevo_estado = self._obtener_nuevo_estado()
            self._agregar_transicion(nuevo_estado, char, None)
            stack.append(nuevo_estado)

    def _agregar_transicion(self, estado_actual, simbolo, estado_siguiente):
        if estado_actual not in self.transiciones:
            self.transiciones[estado_actual] = {}
        self.transiciones[estado_actual][simbolo] = estado_siguiente
        self.estados.add(estado_actual)
        if estado_siguiente:
            self.estados.add(estado_siguiente)

    def _obtener_nuevo_estado(self):
        nuevo_estado = f'q{len(self.estados)}'
        self.estados.add(nuevo_estado)
        return nuevo_estado

    def crear_grafo(self):
        g = Digraph('G')
        for estado in self.estados:
            g.node(estado)

        for estado, transiciones in self.transiciones.items():
            for simbolo, next_state in transiciones.items():
                g.edge(estado, next_state, label=simbolo)

        return g


