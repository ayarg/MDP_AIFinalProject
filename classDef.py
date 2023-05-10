# In this file the definition of the class for MDP will be implemented 

#Representation of a state
class MDPState : 
    """This object represent one state of the MDP, identify by a unique name """

    def __init__(self, name: str, goal: bool):
        """A state is defined by its unique name and a boolean true the state is  a goal of the MDP"""
        self.name = name 
        self.goal = goal
    
    def __eq__(self, other) -> bool :
        """Return true if both states are equal"""
        return (self.name == other.name)



# Representation of an action
class MDPAction : 
    """This object represent an action in the MDP indentified by a cost or reward and its unique name"""

    def __init__(self, name: str, cost: float):
        """An action is defined by its unique name and its cost"""
        self.name = name 
        self.cost = cost 
    

# Representation of transition 
class MDPTransition : 
    """This object represent the probability of  transition between two states using one action"""

    def __init__(self, state_from : MDPState, state_to : MDPState, action : MDPAction, transition_probability : float):
        """A transition is represented by a state_from, a state_to, an action and a transition_probability in [0,1]"""
        self.state_from = state_from
        self.state_to = state_to
        self.transition_probability = transition_probability

        # if self.transition_probability not in [0,1] raise error 

# Represent a set of transitions 
class MDPTransitionsContainer : 
    """This object represent a set of MDPTransitions stored in a list setTransition who share the same state_from and action"""
    def __init__(sefl, state_from : MDPState, action : MDPAction):
        """A TranstionContainer is indetifyed by a state_from and an action"""
        self.state_from = state_from
        self.action = action
        self.setTransition = [] # create an empty list for each Container

    def __addTransition__(self, transition : MDPTransition):
        """Add a transition to the Container"""
        if ( transition in self.setTransition == 0  ):  # Check if the element isn't in the set before adding it
            self.setTransition.append(transition)
    
    def __deleteTransition__ (self, transition : MDPTransition):
        """Delete a transition to the Container"""
        if ( transition in self.setTransition ):
            self.setTransition.remove(transition)


   '''     
    def partialExpectedCost (self, V : list) -> float :
        """Compute a part of the bellman equation : 
        cost(a)+ sum(P(s'|s,a)) where 
        s = self.state_from, 
        a = self.action
        and P(s'|s,a) are every transition in the cContainer
        input : V a list of the expected cost 
        output : a float """

        cost = self.action.cost 
        n = len(n) 
    '''
        