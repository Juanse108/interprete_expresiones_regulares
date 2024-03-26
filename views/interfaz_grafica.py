from tkinter import *


class InterfazGrafica(Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # Implementación de la interfaz gráfica
        # utilizando la biblioteca tkinter

        # Métodos para:
        #   * Mostrar la expresión regular
        #   * Mostrar el autómata
        #   * Mostrar la información del autómata
        #   * Permitir al usuario ingresar la expresión regular
        #   * Permitir al usuario simular el autómata con una cadena de entrada
