# -*- coding: utf-8 -*-
"""
@author: Gowtham Bharadwaj 801101552
         Medha Nagaraj 801101751
"""

import random,copy
iterate = 0
solution = True
randomRestart = 0
stepsClimbed = 0
passedboard = None

#This method prints the configuration of the N-Queen Puzzle
def printBoard(state):
   for l in range(0,N):
          for m in range(0,N):
              if m < N-1:
                  print(state[l][m], end=" ")
              elif(m == N-1):
                  print(state[l][m], end="\n") 
 
#Class definition of the Queen
class queenPuzzle:
  #Method definition to intialize the variables required to track the result
  def __init__(self, searchCategory, iterate, solution):
    #Initialize the required variables and counters
    self.totalRuns = iterate
    self.totalSuccess = 0
    self.totalFail = 0
    self.stepsForSuccess = 0
    self.stepsForFail = 0
    self.sideMove = 0
    
    self.solution = solution
    for i in range(0,iterate):
      if self.solution == True:
        print ("\n----------------------------")
        print ("Board configuration for the run",i+1)
        print ("----------------------------")
      self.queen_board = board(passedboard)
      self.cost = self.attackHeuristic(self.queen_board)
      #Call to the appropriate hill climbing code
      if (searchCategory == 1):
          self.hillClimbing()
      elif (searchCategory == 2):
          self.sideways()
      elif (searchCategory == 3):
          self.randomRestartWithoutSidemove()
      elif (searchCategory == 4):
          self.randomRestartWithSidemove()
 
  #Method for the Steepest hill climbing code
  def hillClimbing(self):
    totalSteps = 0
    while 1:
      current_attacks = self.cost
      #Breaking if the random initial state itself is a sucess state
      if self.cost == 0:
          break
      #Call the optimal board
      self.optimalBoard()
      if (current_attacks == self.cost):
        self.totalFail += 1
        self.stepsForFail += totalSteps
        if totalSteps == 0:
            self.stepsForFail += 1
        break
      totalSteps += 1
      if self.solution == True:
        print ("\nThe Number of attack pairs is", (int)(self.attackHeuristic(self.queen_board)))
        printBoard(self.queen_board.board)
      if (self.cost == 0):
          break
    #Handle failure - when the solution is not found
    if self.cost != 0:
      if self.solution == True:
        print ("\n*****NO SOLUTION*****")
    #Handle failure - when the solution is found
    else:
      if self.solution == True:
        print ("\n*****SOLUTION FOUND*****")
      self.totalSuccess += 1
      self.stepsForSuccess += totalSteps
    return self.cost

  #Method definition for the Sideways hill climbing Algorithm
  def sideways(self):
    totalSteps = 0
    sideMove = 0
    while 1:
      current_attacks = self.cost
      current_board = self.queen_board
      #Breaking if the random initial state itself is a sucess state
      if self.cost == 0:
          break
      #Call to generare the sucessesor board that can return both equal heuristic board or lower heuristic board
      self.successorBoard()
      if current_board == self.queen_board:
          self.stepsForFail += totalSteps
          self.totalFail += 1
          if totalSteps == 0:
            self.stepsForFail += 1
          break
      if current_attacks == self.cost:
        sideMove += 1
        if sideMove == 100:
            self.stepsForFail += totalSteps
            self.totalFail += 1
            break
      elif(current_attacks > self.cost):
          sideMove = 0
      totalSteps += 1
      if self.solution == True:
        print ("\nThe Number of attack pairs is", (int)(self.attackHeuristic(self.queen_board)))
        printBoard(self.queen_board.board)
      if self.cost == 0:
        break
    if self.cost != 0:
      if self.solution == True:
        print ("\n***** NO SOLUTION *****")
    else:
      if self.solution == True:
        print ("\n***** SOLUTION FOUND *****")
      #Increment the count of the number of success incurred and total steps taken for each successful iteration
      self.totalSuccess += 1
      self.stepsForSuccess += totalSteps
    return self.cost

  #Definition for the Random Restart without sideways allowing  hill climbing Algorithm  
  def randomRestartWithoutSidemove(self): 
      while 1:        
        current_attacks = self.cost
        current_board = self.queen_board
        #Breaking if the random initial state itself is a sucess state
        if self.cost == 0:
            break
        #Call to generare the sucessesor board
        self.optimalBoard()
        #Check and logic for random Restart
        if (current_board == self.queen_board) or ((current_attacks == self.cost) & (self.cost != 0)):
          self.queen_board = board(passedboard)
          global randomRestart
          #Increment the Random Restarts counter
          randomRestart += 1 
          self.cost = self.attackHeuristic(self.queen_board)               
        elif (self.cost < current_attacks):  
            if self.solution == True:
                print ("\nThe Number of attack pairs is", (int)(self.attackHeuristic(self.queen_board)))
                printBoard(self.queen_board.board)
        global stepsClimbed
        #Increment the Steps counter in Random restart Hill climbing algorithm
        stepsClimbed += 1 
        if self.cost == 0:
          break     
      if self.solution == True:
          print ("\n***** SOLUTION FOUND *****")
           #Incrementing the count for number of success incurred
      self.totalSuccess += 1     
      return self.cost
  
  #Definition for the Random Restart with sideways allow hill climbing Algorithm  
  def randomRestartWithSidemove(self):
      sideMove = 0
      while 1:        
        current_attacks = self.cost
        current_board = self.queen_board
        #Breaking if the random initial state itself is a sucess state
        if self.cost == 0:
            break
        #Call to generare the sucessesor board
        self.successorBoard()
        #Check and logic for random Restart
        if current_board == self.queen_board:
          self.queen_board = board(passedboard)
          global randomRestart
          #Increment the Random Restarts counter
          randomRestart += 1 
          self.cost = self.attackHeuristic(self.queen_board) 
        if current_attacks == self.cost:
          sideMove += 1
          if sideMove == 100:
            self.queen_board = board(passedboard)
            #Increment the Random Restarts counter
            randomRestart += 1 
            self.cost = self.attackHeuristic(self.queen_board)
        elif(current_attacks > self.cost):
          sideMove = 0
        global stepsClimbed
        #Increment the Steps counter in Random restart Hill climbing algorithm
        stepsClimbed += 1    
        if self.solution == True:
          print ("\nThe Number of attack pairs is", (int)(self.attackHeuristic(self.queen_board)))
          printBoard(self.queen_board.board)
        if self.cost == 0:
          break     
      if self.solution == True:
          print ("\n***** SOLUTION FOUND *****")
           #Incrementing the count for number of success incurred
      self.totalSuccess += 1     
      return self.cost
 
  #Print Definition exclsive to each type of Hill climbing algorithm
  def ReportStatistics(self):
    print ("\nTotal number of runs is", self.totalRuns)
    print ("Total Success: ", self.totalSuccess)
    print ("Success rate: ", (float(self.totalSuccess)/float(self.totalRuns))*100,"%")
    
    #Print statements for Steepest Hill climbing Algorithm 
    # & Sideways Hill climbing Algorithm
    if(searchCategory == 1) or (searchCategory == 2):
        print ("Total Fail: ", self.totalFail)
        print ("Failure rate: ", (float(self.totalFail)/float(self.totalRuns))*100,"%")
        if(self.totalSuccess >= 1):
          print ("Average number of steps in success: ", float(self.stepsForSuccess)/float(self.totalSuccess))
          print ("Total Steps for Success: ", self.stepsForSuccess)
        if(self.totalFail >= 1):
          print ("Total Steps for Fail: ", self.stepsForFail)
          print ("Average number of steps when failed: ", float(self.stepsForFail)/float(self.totalFail))
          
    #Print statements for Random Restart Hill climbing Algorithm
    if(searchCategory == 3) or (searchCategory == 4):
        print ("Total number of random restarts:", randomRestart)
        print ("Average number of random restarts: ", float(randomRestart)/float(self.totalRuns))
        print ("Average number of steps: ", float(stepsClimbed)/float(self.totalRuns));
    
  #Definition for calculating the number of attack pairs     
  def attackHeuristic(self, temp_board):
    #these are separate for easier debugging
    straight_attacks = 0
    diagonal_attacks = 0
    for i in range(0,N):
      for j in range(0,N):
        #If the Queen node is encountered then calculate all of the attack pairs
        if temp_board.board[i][j] == "Q":
          #Subtract the total cost by 2 so that we don't count the self state
          straight_attacks -= 2
          for k in range(0,N):
            if temp_board.board[i][k] == "Q":
              straight_attacks += 1
            if temp_board.board[k][j] == "Q":
              straight_attacks += 1
          #Calculate all the diagonal attacks
          k, l = i+1, j+1
          while k < N and l < N:
            if temp_board.board[k][l] == "Q":
              diagonal_attacks += 1
            k +=1
            l +=1
          k, l = i+1, j-1
          while k < N and l >= 0:
            if temp_board.board[k][l] == "Q":
              diagonal_attacks += 1
            k +=1
            l -=1
          k, l = i-1, j+1
          while k >= 0 and l < N:
            if temp_board.board[k][l] == "Q":
              diagonal_attacks += 1
            k -=1
            l +=1
          k, l = i-1, j-1
          while k >= 0 and l >= 0:
            if temp_board.board[k][l] == "Q":
              diagonal_attacks += 1
            k -=1
            l -=1
    return ((diagonal_attacks + straight_attacks)/2)
 
  #This function tries moving every queen to every spot, with only one move
  #and returns the move that has the least number of attacks pairs
  def optimalBoard(self):
    least_cost = self.attackHeuristic(self.queen_board)
    most_desirable = self.queen_board
    #We move one queen at a time
    for q_col in range(0,N):
      for q_row in range(0,N):
        if self.queen_board.board[q_row][q_col] == "Q":
          #We get the lowest cost configuration by moving each queen in its respective column
          for m_row in range(0,N):
              if self.queen_board.board[m_row][q_col] != "Q":
                #Queen is placed in empty slot of each column
                test_board = copy.deepcopy(self.queen_board)
                test_board.board[q_row][q_col] = "-"
                test_board.board[m_row][q_col] = "Q"
                test_board_cost = self.attackHeuristic(test_board)
                if test_board_cost < least_cost:
                  least_cost = test_board_cost
                  most_desirable = test_board
    self.queen_board = most_desirable
    self.cost = least_cost
 
  #This function tries moving every queen to every spot, with only one move
  #and returns the move that has the least number of attacks pairs or if not 
  #then it will atleast try to send the state with same heuristic
  def successorBoard(self):
    equal_h_count = 0
    equi = {}
    presentcost = self.attackHeuristic(self.queen_board)
    least_cost = self.attackHeuristic(self.queen_board)
    most_desirable = self.queen_board
    #move one queen at a time, the optimal single move by brute force
    for q_col in range(0,N):
      for q_row in range(0,N):
        if self.queen_board.board[q_row][q_col] == "Q":
          #get the lowest cost by moving this queen
          for m_row in range(0,N):
              if self.queen_board.board[m_row][q_col] != "Q":
                #try placing the queen here and see if it's any better
                test_board = copy.deepcopy(self.queen_board)
                test_board.board[q_row][q_col] = "-"
                test_board.board[m_row][q_col] = "Q"
                test_board_cost = self.attackHeuristic(test_board)
                if test_board_cost < least_cost:
                  least_cost = test_board_cost
                  most_desirable = test_board
                if test_board_cost == presentcost:
                  equi[equal_h_count] = test_board
                  equal_h_count += 1
    if least_cost == presentcost:
        print("Number of successors with heuristic value same as that of the current state:", equal_h_count)
        if(equal_h_count == 1):
            most_desirable = equi[0]  
        elif(equal_h_count > 1):
            rand_ind = random.randint(0,equal_h_count - 1)
            print("Random index chooses one of the successors with same heuristic value:", rand_ind)
            most_desirable = equi[rand_ind]
    self.queen_board = most_desirable
    self.cost = least_cost

#Class for the Board
class board:
  #Intialize Method which will generate a random initial state
  def __init__(self, list=None):
    if list == None:
      self.board = [["-" for i in range(0,N)] for j in range(0,N)]
      #initialize queens at random places
      for j in range(0,N):
        rand_row = random.randint(0,N-1)
        if self.board[rand_row][j] == "-":
          self.board[rand_row][j] = "Q"
      print("\nInitial Configuration:")
      printBoard(self.board)
    

#Main Method which will call a proper hill climbing variant based on users input
if __name__ == "__main__":
  print ("\n********** N Queen Puzzle Solution *********\n")
  print ("\nEnter the number of queens on the board (N): ")
  N = int(input())    
  print ("\nIteration Count Selection: \nChoose \n1. To solve the puzzle for 500 times\n2. To determine how many times you would like to run the code ")
  iterationChoice = int(input())
  if (iterationChoice == 1):
      iterate = 500      
  elif (iterationChoice == 2):
      print ("\nPlease Enter the required number of runs: ")
      iterate = int(input())
  else:
      iterate = 500 
      print ("\nInvalid Choice")
      print ("\nTaking the default value of 500 iterations \n")
  print ("\nSearch type: \nChoose \n1. Steepest Ascent Hill Climbing\n2. Hill Climbing with Sideways Move\n3. Random-Restart Hill Climbing without Sidemove\n4. Random-Restart Hill Climbing with Sidemove")
  searchStrategy = int(input())
  if (searchStrategy == 1):
      searchCategory = 1      
  elif (searchStrategy == 2):      
      searchCategory = 2
  elif (searchStrategy == 3):      
      searchCategory = 3   
  elif (searchStrategy == 4):
      searchCategory = 4
  else:
      searchCategory = 1
      print ("\nInvalid Choice")
      print ("\nRunning the default approach - Steepest Ascent Hill Climbing\n")
 
  queen_board = queenPuzzle(searchCategory, iterate, solution)
  queen_board.ReportStatistics()
