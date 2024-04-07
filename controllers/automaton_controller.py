from models.reader import Reader
from models.parsing import Parser
from models.nfa import NFA
from models.dfa import DFA
from models.direct_reader import DirectReader
from models.direct_dfa import DDFA
from views.console_view import ConsoleView


class AutomatonController:
    def __init__(self, regex):
        self.regex = regex
        self.nfa = None
        self.dfa = None
        self.ddfa = None

    def generate_nfa(self):
        reader = Reader(self.regex)
        tokens = reader.CreateTokens()
        parser = Parser(tokens)
        tree = parser.Parse()
        self.nfa = NFA(tree, reader.GetSymbols(), self.regex)
        return self.nfa

    def generate_dfa(self):
        if not self.nfa:
            self.generate_nfa()
        self.dfa = DFA(self.nfa.trans_func, self.nfa.symbols, self.nfa.curr_state, self.nfa.accepting_states,
                       self.regex)
        self.dfa.TransformNFAToDFA()
        return self.dfa

    def generate_ddfa(self):
        direct_reader = DirectReader(self.regex)
        direct_tokens = direct_reader.CreateTokens()
        direct_parser = Parser(direct_tokens)
        direct_tree = direct_parser.Parse()
        self.ddfa = DDFA(direct_tree, direct_reader.GetSymbols(), self.regex)
        return self.ddfa


