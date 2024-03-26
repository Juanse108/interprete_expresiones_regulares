import re


class ExpresionRegular:
    def __init__(self, expresion_regular):
        self.expresion_regular = expresion_regular

    def get_expresion_regular(self):
        return self.expresion_regular

    def get_numero_estados(self):
        # Implementación básica: cuenta los paréntesis como indicadores de estados
        return self.expresion_regular.count("(") + self.expresion_regular.count(")")

    def get_numero_transiciones(self):
        # Implementación básica: cuenta los símbolos de transición (excepto los meta-caracteres)
        alfabeto = self.get_alfabeto()
        return len(re.findall(f"[{re.escape(''.join(alfabeto))}]", self.expresion_regular))

    def get_alfabeto(self):
        # Implementación básica: extrae los caracteres individuales, excluyendo meta-caracteres
        alfabeto = set()
        for caracter in self.expresion_regular:
            if caracter.isalnum():
                alfabeto.add(caracter)
        return alfabeto
