from controllers.controller import Controller

if __name__ == "__main__":
    try:
        controller = Controller()
        controller.run()
    except Exception as e:
        print(f"Un error ha ocurrido inesperado : {e}")
