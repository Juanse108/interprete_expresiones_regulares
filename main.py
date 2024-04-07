from controllers.automaton_controller import AutomatonController
from views.console_view import ConsoleView

if __name__ == "__main__":
    ConsoleView.display_title()
    opt = None
    regex = None
    method = None
    controller = None

    while opt != 0:
        ConsoleView.display_type_regex_msg()
        regex = input('> ')
        try:
            controller = AutomatonController(regex)

        except Exception as e:
            print(f'\n\tERR: {e}')

        if not regex:
            print('\n\tERR: You need to set a regular expression first!')
            opt = None
        else:
            print('\n\tExpression accepted!')
            ConsoleView.display_submenu()
            method = input('> ')

            if method == '1':
                nfa = controller.generate_nfa()
                dfa = controller.generate_dfa()
                nfa.WriteNFADiagram()
                dfa.GraphDFA()

            elif method == '2':
                ddfa = controller.generate_ddfa()
                ddfa.GraphDFA()

            elif method == '0':
                exit(1)

            else:
                ConsoleView.display_invalid_option_msg()
