class MDPReader:
    #The purpose of this class is reading the MDP text file, which contains actions, transitions and states values
     def __init__(self, mdp_file):
        self.states = set()
        self.actions = set()
        self.transitions = {}
        mdp_file = open('MDP.txt', 'r')
        with open(mdp_file, 'r') as file:
        for line in file:
                if line.startswith('states'):
                    state = line.split()[1]
                    self.states.add(state)
                elif line.startswith('action'):
                    action = line.split()[1]
                    self.actions.add(action)
                elif line.startswith('transition'):
                    parts = line.split()
                    state = parts[1]
                    action = parts[2]
                    next_state = parts[3]
                    reward = float(parts[4])
                    probability = float(parts[5])
                    if state not in self.transitions:
                        self.transitions[state] = {}
                    if action not in self.transitions[state]:
                        self.transitions[state][action] = {}
                    self.transitions[state][action][next_state] = (reward, probability)
     def get_transition(self, state, action):
        if state in self.transitions and action in self.transitions[state]:
            return self.transitions[state][action]
        else:
            return {}
