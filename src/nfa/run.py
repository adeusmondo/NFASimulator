from src.nfa.engine import NFA
from src.nfa import consts

def run():
  nfa = NFA(definition=consts.DEFINITION_AUTOMATON_PATH)
  nfa.read_inputs(path=consts.INPUTS_PATH)
  nfa.process()