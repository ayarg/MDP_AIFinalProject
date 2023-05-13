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
    
    def __str__(self) : 
        if (self.goal == True):
            return(self.name + ' GOAL')
        else :
            return(self.name)



# Representation of an action
class MDPAction : 
    """This object represent an action in the MDP indentified by a cost or reward and its unique name"""

    def __init__(self, name: str, cost: float):
        """An action is defined by its unique name and its cost"""
        self.name : str = name 
        self.cost :float = cost 
    
    def __str__(self):
        return ('('+self.name + ', '+ str(self.cost)+')')

# Representation of transition 
class MDPTransition : 
    """This object represent the probability of  transition between two states using one action"""

    def __init__(self, state_from : MDPState, state_to : MDPState, action : MDPAction, probability : float):
        """A transition is represented by a state_from, a state_to, an action and a transition_probability in [0,1]"""
        self.state_from : MDPState = state_from
        self.state_to : MDPState = state_to
        self.action : MDPAction = action
        self.probability : float = probability
            # TO DO : if probability not in [0,1] raise error 
    def __str__ (self):
        return ( self.state_from.__str__()+' | '+ self.action.__str__()+' | '+ self.state_to.__str__() + ' | '+ str(self.probability))
        #print('{',self.state_from.__toString__(),self.action.__toString__(),self.state_to.__toString__(),self'}')

# Represent a set of transitions 
class MDPTransitionsContainer : 
    """This object represent a set of MDPTransitions who share the same state_from 
    stored in a dictionnary Transitions indexed by action's name
    action_name : [Transition1, Transition2, ...]
    

    """
    #TO DO: complete the comment 
    
    def __init__(self, state_from : MDPState):
        """A TranstionContainer is indetifyed by a state_from"""
        self.state_from = state_from

        self.Transitions = {} # dictionnary with key as action and value as list of possible transition
        
        # self.setTransition = [] # create an empty list for each Container

    def __str__(self):
        char = 'Possible transition from State ' + self.state_from.__str__() + ' are :' +'\n'
        for key, mylist in self.Transitions.items() :
            char +=  'using action ' + mylist[0].action.__str__() +'\n'
            for t  in mylist :
                t : MDPTransition 
                char += t.__str__() +'\n'
        return  char

    def __addTransition__(self, transition : MDPTransition):
        """Add a transition to the dictionnary Transitions"""
        if (transition.state_from == self.state_from ) :
            key = transition.action.name
            if (key in self.Transitions):
                self.Transitions[key] += [transition]
            else :
                self.Transitions[key] = [transition] 
            

    def __deleteTransition__ (self, transition : MDPTransition):
        """Delete a transition to the Container"""
        if ( transition in self.setTransition ):
            self.setTransition.remove(transition)


        
    def iterExpectedCost (self, V : dict) -> float :
        #TO DO : rewritte the comment
        """Compute an Vi+1(s) of the bellman equation  for the state knowing Vi(all states): 
        cost(a)+ sum(P(s'|s,a)) where 
        and P(s'|s,a) are every transition in the dictionnary Transitions
        input : V a dictionnary of the expected cost (Vi of all states)  state : value
        output : a float ( Vi+1(s))"""
        if (self.state_from.goal == False): 
            #minimum : float = V[self.state_from.name] #initialize Vi+1 to Vi bcs Vi+1=<Vi
            minimum = 20
            #TO DO : find a value to initialize  minimum
            for myaction, mylist in self.Transitions.items():
                cost :float  = mylist[0].action.cost   # my_list contains every transition from state_from using action action                
                sum :float  = cost
                #print('action', mylist[0].action.__str__())
                for t  in mylist :              # t is a Transition from my_list 
                    t : MDPTransition
                    #print(t)
                    if ( t.state_to.name in V ):
                        sum = sum + t.probability * V[t.state_to.name]
                        #print('sum : ',sum)
                minimum = min(minimum, sum) 
            print(self.state_from.name, minimum )
            return minimum
            
        else : 
            return 0    

    def optimalPolicyState ( self, V:dict)-> MDPAction :
        """This function return the optimal policy of one state knowing the expected cost
        the optimal policy is computed using Belllman equation """
        #TO DO if state_from == goal, return actionNuLL
        #minimum = #initialize Vi+1 to Vi bcs Vi+1=<Vi
        minimum = 20
        for myaction, mylist in self.Transitions.items():
            cost = mylist[0].action.cost   # my_list contains every transition from state_from using action action
            sum = cost
            for t in mylist :              # t is a Transition from my_list 
                if t.state_to.name in V.keys() :
                    sum = sum + t.probability * V[t.state_to.name]
            if (sum < minimum):
                optimalAction = myaction
                minimum = sum 
        return optimalAction     
    
        

# Represent the whole MDP variables
class MDPSystem :
    """ The main class of the package. MDPSystem """

    dico={}
    eps =0.1
    #def __init__(self) : 
    #    self.dico={}

    def __add_MDPTransitionsContainer__ (self, container : MDPTransitionsContainer):
        self.dico[container.state_from.name]=container
        print('container', container.__str__(), 'added')

    def __remove_MDPTransitionsContainer__ (self, name_state : str):
        del self.dico[name_state]

    def __str__(self):
        char = 'Le system est composé de : ' +'\n'
        for key, container in self.dico.items():
            char += '\n'+ container.__str__()
        print (char)


    def expectedPolicy (dico : dict, eps : float)->dict :
        """Compute the expected Policy for each state of the MDP using bellman equation
        input : a dict  state_name : MDPTransitionContainer of the state 
        output : a dict state_name : V(state)"""
    
        #TO DO : check eps>0

        V={}
        for key in dico : 
            V[key] = 0
        W = V.copy()
        err = 3*eps
        iter = 0 
        while (err > eps and iter<30): 
            err = 0
            for myState, myContainer in dico.items() :
                W[myState]=myContainer.iterExpectedCost(V)
                err = max(err, abs(V[myState]-W[myState]))
            V=W.copy()
            iter += 1
        print('expected policy', V, 'err', err)
        return V 
    
    def optimalPolicy (self, eps:float) -> dict :
        """Compute the Optimal Policy of all states using bellman equation 
        input : a dict  state_name : MDPTransitionContainer of the state 
        output : a dict state_name : PI(state)"""
        
        V =  self.expectedPolicy (self.dico, eps)

        PI = {}
        for key , container in self.dico.items() : 
            PI[key] = container.optimalPolicyState(V)
        print('optimal policy :',PI)
        return PI
        


        

