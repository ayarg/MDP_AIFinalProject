import numpy as np
Temp = np.linspace(16,25,19)
n=19
cost=[1,0]
print(cost)


#this function is to calculate the expected cost using the MDP formula
def expectedCost(n,na,CPT, cost, eps, goal):
    V = [0]*n
    W=[0]*n
    eps = abs(eps)
    err = 3*eps
    iter =0
    while(err>eps) : 
        iter = iter+1
        for s in range(n):
            if (s!=goal):
                B=[]
                for a in range(na): 
                    P = CPT[a][s]
                    #print('s,a=',s,a,' Pa= ',P)
                    if (P!=[]):  # if P=[] it means from s we can not do the action a
                        B.append( cost[a] + sum([p*v for p,v in zip(P,V)]) )
                #print('B= ',B)                 
                W[s]=min(B) 
            else :
                W[s]=0
        err = max(abs(v-w) for v,w in zip(V,W))
        V = W.copy()
        #print('iter =',iter,'V=',V)
        #print( 'err= ',err)
    #print('Vresult= ',V)
    return V 



#this function is to select the optimal policy according to MDP odel
def optimalPolicy(n,na,CPT, cost, eps, goal,V):
    V = [0]*n
    W=[0]*n
    eps = abs(eps)
    err = 3*eps
    PI=[0]*n

    for s in range(n):
        if (s!=goal):
            B=[-1]*na
            for a in range(na): 
                P = CPT[a][s]
                print('s,a=',s,a,' Pa= ',P)
                if (P!=[]):  # if P=[] it means from s we can not do the action a
                    B[a]=( cost[a] + sum([p*v for p,v in zip(P,V)]) )
            print('B= ',B)                 
            PI[s]=B.index(min([a for a in B if a>=0])) 
        else :
            PI[s]='goal'
    return PI
