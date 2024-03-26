from graphviz import Digraph


class Automata:
    def __init__(self, expresion_regular):
        self.expresion_regular = expresion_regular
        self.grafo = self._crear_grafo()

    def _crear_grafo(self):
        """Implementación de la creación del grafo que representa el autómata
        utilizando la biblioteca graphviz"""

    def get_informacion(self):
        """Implementación de la obtención de información del autómata
        (estados, transiciones, etc.)"""

    def simular(self, cadena_entrada):
        """Implementación de la simulación del autómata con una cadena de entrada
        y la obtención del resultado de la simulación"""
