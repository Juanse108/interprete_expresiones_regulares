from utils.utils import WriteToFile


class ConsoleView:
    @staticmethod
    def display_title():
        print('''
#        FINITE AUTOMATA        #

Generate NFA's of DFA's based on a regular expression and compare times simulating a string! NOTE: for epsilon expression, please use the letter "e"
''')

    @staticmethod
    def display_submenu():
        print('''
Select one of the above to test your regular expression:

    1. Use Thompson to generate an NFA and Powerset construction to generate an DFA.
    2. Use direct DFA method.
    0. Back to the main menu.
''')

    @staticmethod
    def display_thompson_msg():
        print('''
    # THOMPSON AND POWERSET CONSTRUCTION # ''')

    @staticmethod
    def display_direct_dfa_msg():
        print('''
    # DIRECT DFA CONSTRUCTION # ''')

    @staticmethod
    def display_invalid_option_msg():
        print('''
Err: That's not a valid option!
''')

    @staticmethod
    def display_generate_diagram_msg():
        print('''
Would you like to generate and view the diagram? [y/n] (default: n)''')

    @staticmethod
    def display_type_regex_msg():
        print('''
Type in a regular expression ''')

    @staticmethod
    def display_type_string_msg():
        print('''
Type in a string ''')

    @staticmethod
    def display_dfa_graph(graph):
        graph.attr(rankdir='LR')
        source = graph.source
        WriteToFile('tests/DFA.gv', source)
        graph.render('tests/DFA.gv', format='pdf', view=True)

    @staticmethod
    def display_ddfa_graph(graph):
        graph.attr(rankdir='LR')

        source = graph.source
        WriteToFile('tests/DirectDFA.gv', source)
        graph.render('tests/DirectDFA.gv', format='pdf', view=True)
