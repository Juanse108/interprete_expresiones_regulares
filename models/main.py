from reader import Reader
from parsing import Parser
from nfa import NFA
from dfa import DFA
from direct_dfa import DDFA
from direct_reader import DirectReader

class AutomatonGenerator:
    def __init__(self, regex):
        self.reader = Reader(regex)
        tokens = self.reader.CreateTokens()
        parser = Parser(tokens)
        self.tree = parser.Parse()

    def generate_nfa(self):
        return NFA(self.tree, self.reader.GetSymbols(), regex)

    def generate_dfa(self):
        nfa = self.generate_nfa()
        dfa = DFA(nfa.trans_func, nfa.symbols, nfa.curr_state, nfa.accepting_states, regex)
        dfa.TransformNFAToDFA()
        return dfa

if __name__ == "__main__":
    program_title = '''
#        FINITE AUTOMATA        #

Generate NFA's of DFA's based on a regular expression and compare times simulating a string! NOTE: for epsilon expression, please use the letter "e"
'''

    submenu = '''
Select one of the above to test your regular expression:

    1. Use Thompson to generate an NFA and Powerset construction to generate an DFA.
    2. Use direct DFA method.
    0. Back to the main menu.
'''
    thompson_msg = '''
    # THOMPSON AND POWERSET CONSTRUCTION # '''
    direct_dfa_msg = '''
    # DIRECT DFA CONSTRUCTION # '''
    invalid_opt = '''
Err: That's not a valid option!
'''
    generate_diagram_msg = '''
Would you like to generate and view the diagram? [y/n] (default: n)'''
    type_regex_msg = '''
Type in a regular expression '''
    type_string_msg = '''
Type in a string '''

    print(program_title)
    opt = None
    regex = None
    method = None

    while opt != 0:
        print(type_regex_msg)
        regex = input('> ')

        try:
            generator = AutomatonGenerator(regex)

            direct_reader = DirectReader(regex)
            direct_tokens = direct_reader.CreateTokens()
            direct_parser = Parser(direct_tokens)
            direct_tree = direct_parser.Parse()
            print('\n\tExpression accepted!')
            print('\tParsed tree:', generator.tree)

        except AttributeError as e:
            print(f'\n\tERR: Invalid expression (missing parenthesis)')

        except Exception as e:
            print(f'\n\tERR: {e}')

        if not regex:
            print('\n\tERR: You need to set a regular expression first!')
            opt = None
        else:
            print(submenu)
            method = input('> ')

            if method == '1':
                nfa = generator.generate_nfa()
                dfa = generator.generate_dfa()
                nfa.WriteNFADiagram()
                dfa.GraphDFA()

            elif method == '2':
                ddfa = DDFA(direct_tree, direct_reader.GetSymbols(), regex)
                ddfa_regex = ddfa.EvalRegex()
                ddfa.GraphDFA()
                ddfa = None

            elif method == '0':
                exit(1)

            else:
                print(invalid_opt)
