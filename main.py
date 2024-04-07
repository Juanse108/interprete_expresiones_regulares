from graphviz import Digraph
from controllers.controller import Controller

if __name__ == "__main__":
    try:
        controller = Controller()
        controller.run()
    except Exception as e:
        print(f"Un error inesperado ha ocurrido: {e}")
