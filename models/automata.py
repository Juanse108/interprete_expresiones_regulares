from graphviz import Digraph

from models.expresion_regular import ExpresionRegular


class Automata:
    def __init__(self, expresion_regular):
        self.expresion_regular = ExpresionRegular(expresion_regular)
        self.estados = self.expresion_regular.get_estados()
        self.transiciones = self.expresion_regular.get_transiciones()
        self.estado_inicial = 'q0'
        self.estados_finales = self.expresion_regular.get_estado_final()
        self.grafo = self.crear_grafo()

    def crear_grafo(self):
        g = Digraph('G')
        for estado in self.estados:
            g.node(estado)

        for estado, transiciones in self.transiciones.items():
            for simbolo, next_state in transiciones.items():
                g.edge(estado, next_state, label=simbolo)

        return g

    def get_informacion(self):
        """Returns information about the automaton."""
        informacion = {
            "estados": self.estados,
            "transiciones": self.transiciones,
            "alfabeto": self.get_alfabeto(),
            "estado_inicial": self.estado_inicial,
            "estados_finales": self.estados_finales,
        }
        return informacion

    def get_alfabeto(self):
        """Returns the alphabet (set of unique symbols) used in the automaton."""
        alfabeto = set()
        for estados, transiciones in self.transiciones.items():
            for simbolo, _ in transiciones.items():
                alfabeto.add(simbolo)
        return alfabeto


class AFN(Automata):
    def __init__(self, expresion_regular):
        super().__init__(expresion_regular)


class AFD(Automata):
    def __init__(self, expresion_regular):
        super().__init__(expresion_regular)

