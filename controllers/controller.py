from models.expresion_regular import ExpresionRegular
from models.automata import Automata
from views.interfaz_grafica import InterfazGrafica

class Controller:
    def __init__(self):
        self.expresion_regular = None
        self.automata = None
        self.interfaz_grafica = InterfazGrafica(self)

    def run(self):
        self.interfaz_grafica.mainloop()

    def validar_expresion_regular(self, expresion_regular):
        try:
            ExpresionRegular(expresion_regular)
            return True
        except ValueError:
            return False

    def crear_automata(self, expresion_regular):
        self.expresion_regular = ExpresionRegular(expresion_regular)
        self.automata = Automata(self.expresion_regular)

    def obtener_informacion_automata(self):
        return self.automata.get_informacion()

    def simular_automata(self, cadena_entrada):
        return self.automata.simular(cadena_entrada)
