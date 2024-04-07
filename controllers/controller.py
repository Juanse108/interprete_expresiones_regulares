from models.automata import AFN, AFD, Automata
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
            import re
            re.fullmatch(expresion_regular, "")
            return True
        except ValueError:
            return False

    def crear_automata(self, expresion_regular, tipo_automata):
        """Crea un autómata a partir de una expresión regular y devuelve información sobre el mismo."""
        try:
            # Validar la expresión regular
            if not self.validar_expresion_regular(expresion_regular):
                raise ValueError("Expresión regular no válida")

            # Crear el autómata (AFN o AFD)
            if tipo_automata == "AFN":
                automata = AFN(expresion_regular)
            else:
                automata = AFD(expresion_regular)

            # Obtener información del autómata
            informacion = automata.get_informacion()

            return automata, informacion

        except (ValueError, TypeError) as e:
            # Mostrar mensaje de error al usuario
            self.interfaz_grafica.mostrar_error(e)
            return None, None

    def obtener_informacion_automata(self):
        return self.automata.get_informacion()


