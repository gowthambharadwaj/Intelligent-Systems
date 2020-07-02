""""
@authors: Gowtham Bharadwaj 801101552
          Medha Nagaraj 801101751
"""

import numpy as np
from copy import deepcopy
import time

def misplacedCost(s, g): #Function to calculate the misplaced tiles
        cost = np.sum(s != g)-1
        if cost > 0:
            return cost
        else:
            return 0

def all(s):
    set=string
        
    return 0 not in [c in s for c in set]

#Generate the board list as the the sequence in optimized steps
def optimalSteps(state):
    optimal = np.array([], int).reshape(-1, 9)
    length = len(state) - 1
    while length != -1:
        optimal = np.insert(optimal, 0, state[length]['board'], 0)
        length = int(state[length]['parent'])
    return optimal.reshape(-1, 3, 3)

# solve the board
def calculate(board, goal):
    moves = np.array(   [   ('up', [0, 1, 2], -3),
                            ('dn', [6, 7, 8],  3),
                            ('lt', [0, 3, 6], -1),
                            ('rt', [2, 5, 8],  1)
                            ],
                dtype=  [  ('move',  str, 1),
                           ('pos',   list),
                           ('delta', int)
                           ]
                        )

    diststate = [ ('board',  list),
                ('parent', int),
                ('g_n',     int),
                ('h_n',     int)
                ]

    # Initial state values
    parent = -1     #Initial parent state
    g_n     = 0
    h_n     = misplacedCost(board, goal)    #Calculate misplaced tiles between the initial state and the goal state
    state = np.array([(board, parent, g_n, h_n)], diststate)    #Initializing state

    #Initialize the priority queue
    dtpri = [  ('pos', int),
                    ('f_n', int)
                    ]

    dgpri = np.array( [(0, h_n)], dtpri)
    while True:
        dgpri = np.sort(dgpri, kind='mergesort', order=['f_n', 'pos'])      #Sort the priority queue
        pos, f_n = dgpri[0]     #Choose the first element from the sorted list to explore
        dgpri = np.delete(dgpri, 0, 0)      #Remove the element that we have explored
        board, parent, g_n, h_n = state[pos]
        board = np.array(board)
        loc = int(np.where(board == 0)[0])      #locate '0' (blank)
        g_n = g_n + 1       #Increase the cost of g(n) by 1
        for m in moves:
            if loc not in m['pos']:
                succ = deepcopy(board)     #Generate the new state as a copy of the current state
                succ[loc], succ[loc + m['delta']] = succ[loc + m['delta']], succ[loc]   #Move the digit
                
                if ~(np.all(list(state['board']) == succ, 1)).any():    #Check if the new configuration is not generated before
                    h_n = misplacedCost(succ, goal)    #Calculate the Misplaced tiles
                    q = np.array(   [(succ, pos, g_n, h_n)], diststate)     #Generate and add the new state to the list
                    state = np.append(state, q, 0)
                    f_n = g_n + h_n                                        #Calculate the value of f(n)
                    q = np.array([(len(state) - 1, f_n)], dtpri)    #Add to the priority queue
                    dgpri = np.append(dgpri, q, 0)

                    if np.array_equal(succ, goal):     #Check if this is the desired goal state
                        print('Goal reached') 
                        return state, len(dgpri)
        

    return state, len(dgpri)


###############################################################################
def body():
    print()
    alist = []
    print ("Using Misplaced Tiles, solving the 8 puzzle:")
    print("Feed the initial board configuration: (Leave a space between each input value)")   #Get the initial state
    string = [int(x) for x in input().split()]  # Enter the desired input state. Leave a blank space in between the input characters. Add '0' for the blank space
    print("\nFeed the goal board configuration: (Leave a space between each input value)")
    alist = [int(x) for x in input().split()]   # Enter the desired input state. Leave a blank space in between the input characters. Add '0' for the blank space
    goal=alist


    if len(string) != 9:
        print('Enter only 9 values')
        return

    board = np.array(list(map(int, string)))
    print (board)
    
    
    tstart=time.time()
    state, explored = calculate(board, goal)
    tend=time.time()
    print()
    print('Total number of nodes generated:', len(state))
    print('Total number of nodes explored: ', len(state) - explored)
    print()
    # Generate the optimized steps and display those steps
    optimal = optimalSteps(state)
    print('Total optimized steps:', len(optimal) - 1)
    print()
    print(optimal)
    print()
    print ("The algorithm took " + str((tend-tstart) * 1000)  + " ms of time. to compute")


###############################################################################
# Main portion of the code
body()


