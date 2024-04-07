# Importar las clases necesarias
from models.automata import AFN, AFD, Automata, ExpresionRegular

expresion_regular = "(a|b)*abb"
exp_regular = ExpresionRegular(expresion_regular)
exp_regular.transformar_a_automata()
exp_regular.imprimir_informacion()
exp_regular.crear_grafo()


