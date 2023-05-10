regexp = r'\d.\d*'  # \d = didgit  'number point number' 
m=re.match(regexp, "GMAC")

m=re.match(regexp, "0.7")

def get_probability(number: str)->str : 
    """given a string, returns the number in it in case any was correctly given """
    if re.match(r'(?P<prob>\d.\d*)', number):
        print('matched !')
    else:
        print('nor matched')


def get_line(line: str)->str:
    """Given a line from the specification file, parse it and 
    return if contents, in case it is correct
     
    A line is correct if and only if it has the following syntaxe
           <from_state> - <action>: <probability> - <to_state> 
    
    states and actions are represented by lowercase letter; probabilities
    are parsed by get_prbability (see above)
    """

    #if ( := re.match(r'[a-z]+\s*-\s*[a-z]*'', line)):
    if (r'(?P<initia_state>[a-z]*-\s*)
        print(m.groups())




def parse(file: str):
""" Parses the given content of the given file which is identified
    by its absolute path. The file is known to exist and also to be readable
     (somebody did it before) 
"""
with open (file) as stream : 
    iline =1
    for iline in stream.readlines():
        if get_line(iline):
            print("here I do my thing")
        else :
            


# I need class for representing states
class MDPState :
    """This object represents information about MDP states, identify by a unique name"""

    def __ed__(self, other)-> bool:
        """Return true if both states are equal"""

#I need representation of actions. Actions are identified by a unique name and a probability 
#which shall be represented as a floating point number between 0 and 1 
class MDPActions : 
    """his object represents information about MDP actions, identify by a unique name and probability"""

    def __init__(self, id: str, p: float):
        """Any action is uniquely identified by a string. The probability is used 
            in the MDP computation""" 
        self._members =[]

    def __ed__(self, other)-> bool:
    """Return true if both actions are equal"""

    def __iadd__(self, other: MDPActions):
    """Adds a row to the actions"""
        
        if other in self._members :
            raise ValueError()
        self._members.append(other)

        return self

#I need also to keep a separate list of transition : First, define a single transition
class MDPTransition :
    """Definition of MDP transitions"""

    def __init__ (self, from_state : MDPState, action : MADPAction, to_state : MDPState):
        """A transition is defined by a starting state, an action and a destination state""""

    def __ed__(self, other)-> bool:
    """Return true if both transitions are equal"""

# I need a container of transitions : 
class MDPTransitions:
    """Definition o a container of MDP Transitions"""

    def __init__ (self):
        """Any container in general can be empty"""
    

    def __len__(self): 
        """Return the number of transitions in the container"""
    
    def __iter__ (self):
        """Return an iterator over the transitions in the container"""

    def __next__(self): 
        """Return the next transition in the container"""







###Script
q is my initial state, a Policy should be computed for it as much as all others. 

actions are enumerated sequentially from 3

q - action1 : 0.3 -s
q - action2 : 0.5 -t
q - action3 : 0.2 -u