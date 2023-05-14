import classDef as md

myMDP = md.MDPSystem(0.1)
myMDP.__readMDP__('TempControl.txt', 0.1)
#print(myMDP)

V = myMDP.expectedPolicy()
print('expected policy',V)
PI = myMDP.optimalPolicy()
print('\noptimal policy: \n',PI)


