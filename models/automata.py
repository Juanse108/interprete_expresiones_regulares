from graphviz import Digraph
from models.expresion_regular import ExpresionRegular


class Automata:
    def __init__(self, expresion_regular):
        self.expresion_regular = ExpresionRegular(expresion_regular)
        self.estados = set()
        self.transiciones = {}
        self.estado_inicial = None
        self.estados_finales = set()
        self.grafo = None

    def _crear_grafo(self):
        """Abstract method to be implemented in subclasses (AFN and AFD)
        for creating the graph representation using graphviz."""
        raise NotImplementedError("Subclass must implement _crear_grafo")

    def get_informacion(self):
        informacion = {
            "estados": self.estados,
            "transiciones": self.transiciones,
            "alfabeto": self.get_alfabeto(),
            "estado_inicial": self.estado_inicial,
            "estados_finales": self.estados_finales,
        }
        return informacion

    def get_alfabeto(self):

        alfabeto = set()
        for estados, transiciones in self.transiciones.items():
            for simbolo, _ in transiciones.items():
                alfabeto.add(simbolo)
        return alfabeto


class AFN(Automata):
    def __init__(self, expresion_regular):
        super().__init__(expresion_regular)
        self._construir_automata_AFN(expresion_regular)  # Build AFN from RE

    def _construir_automata_AFN(self, expresion_regular):
        """Abstract method to be implemented for specific AFN construction logic (e.g., Thompson's construction)."""
        raise NotImplementedError("Subclass must implement _construir_automata_AFN")

    def simular(self, cadena_entrada):
        """Simulates the AFN with an input string using the subset construction algorithm."""
        estados_actuales = {self.estado_inicial}  # Set of current states
        for simbolo in cadena_entrada:
            estados_siguientes = set()
            for estado in estados_actuales:
                if simbolo in self.transiciones.get(estado, {}):
                    estados_siguientes.update(self.transiciones[estado][simbolo])
            estados_actuales = estados_siguientes
        return any(estado in self.estados_finales for estado in estados_actuales)


class AFD(Automata):
    def __init__(self, expresion_regular):
        super().__init__(expresion_regular)
        self._construir_automata_AFD(expresion_regular)  # Build AFD from RE (e.g., subset construction)

    def _construir_automata_AFD(self, expresion_regular):
        """Abstract method to be implemented for specific AFD construction logic
        (e.g., subset construction from an equivalent AFN)."""
        raise NotImplementedError("Subclass must implement _construir_automata_AFD")

    def simular(self, cadena_entrada):
        """Simulates the AFD with an input string using the state transition table."""
        estado_actual = self.estado_inicial
        for simbolo in cadena_entrada:
            if simbolo not in self.transiciones.get(estado_actual, {}):
                return False  # No transition for the symbol, not accepted
            estado_actual = self.transiciones[estado_actual][simbolo]
        return estado_actual in self.estados_finales
