import os

from src.nfa import consts

class NFA:
  def __init__(self, definition: str = None):
    self._info = {
      "states": [], 
      "alphabet": [], 
      "transitions": [], 
      "file_transitions": [],
      "initial_state": None,
      "final_state": [], 
    }
    self._inputs = []
    self._accepted_state = {}

    if os.path.exists(consts.PROCESS_STEPS):
      os.remove(consts.PROCESS_STEPS)
    
    if os.path.exists(consts.ACCEPTED_STATES):
      os.remove(consts.ACCEPTED_STATES)
    
    if definition:
      self.set_definition(path=definition)
  
  @property
  def states(self):
    return self._info.get("states")
     
  @property
  def alphabet(self):
    return self._info.get("alphabet")
    
  @property
  def transitions(self):
    return self._info.get("transitions")
  
  @property
  def final_state(self):
    return self._info.get("final_state")
    
  @property
  def initial_state(self):
    return self._info.get("initial_state")

  @property
  def inputs(self):
    return self._inputs

  @property
  def accepted_state(self):
    return self._accepted_state
  
  def set_definition(self, path: str):
    with open(path, 'r') as f:
      count_lines = len(f.readlines())
      f.seek(0)

      # Lê o conteudo do arquivo e de acordo com o indice dele, determina
      # Qual dado que está sendo definido para o automato
      for idx, line in enumerate(f.readlines()):
        content = line.split("#")[0].strip().split(" ")
        if idx == 0:
          self._info.update(states=content)
          continue
        elif idx == 1:
          self._info.update(alphabet=content)
          continue
        elif idx >= 2 and idx <= (len(self.states) * len(self.alphabet) + 1):
          file_transitions = self._info.get("file_transitions")
          file_transitions.append(content)
          self._info.update(file_transitions=file_transitions)
          continue
        elif idx == (count_lines - 2):
          self._info.update(initial_state=str(content[0]))
          continue
        elif idx == (count_lines - 1):
          self._info.update(final_state=content)

    # Bloco abaixo monta um dicionario com a matrix de transações do Automato
    transitions = {}
    idx = 0
    for state in self.states:
      transitions[state] = {}
      for alphabet in self.alphabet:
        transitions[state][alphabet] = self._info.get("file_transitions")[idx]
        idx += 1
    self._info.update(transitions=transitions)

  def read_inputs(self, path: str):
    """Faz a leitura dos inputs escritos no arquivo para saber quais o NFA
    deve processar
    """
    with open(path, 'r') as f:
      for line in f.readlines():
        self._inputs.append(line.strip())
        self._accepted_state[line.strip()] = {"accepted": None}
  
  def process(self):
    with open(consts.PROCESS_STEPS, 'w') as f:
      for inputs in self.inputs:
        current_states = ""
        next_states = [str(self.initial_state)]

        f.write(f"\n\n-------------\nINPUT : [{inputs}]\n")
        f.write(f"Estado inicial -> {current_states}")
        for alphabet_input in inputs:
          for next_state in next_states:
            current_states += " " + str(next_state)
            if next_state == "*":
              continue
            all_transitions = self._info.get("transitions")
            all_states_transitions = all_transitions.get(next_state)
            transition_states_alphabet_input = all_states_transitions.get(alphabet_input)
            next_states = transition_states_alphabet_input
            f.write(f"\nSimbolo lido -> {alphabet_input}")
            f.write(f"\nEstados correntes -> {current_states}")
            print()
        
        if next_state in self.final_state:
          self._accepted_state[inputs]["accepted"] = True
        else:
          self._accepted_state[inputs]["accepted"] = False
    
    with open(consts.ACCEPTED_STATES, 'w') as f:
      for inputs in self.inputs:
        accepted_state = self._accepted_state.get(inputs).get("accepted")
        f.write(f"INPUT : [{inputs}] -> {accepted_state}\n")

# {
#   'q1': {
#     '0': ['q1'], 
#     '1': ['q2'],
#   }, 
#   'q2': {
#     '0': ['q3'], 
#     '1': ['*'], 
#   }, 
#   'q3': {
#     '0': ['*'], 
#     '1': ['q4'], 
#   }, 
#   'q4': {
#     '0': ['q4'], 
#     '1': ['q4'], 
#   }
# }
# 010010110
# 010101
# q1 . q1 .
# INICIAL : q1
# FINAL : q4