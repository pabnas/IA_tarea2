# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import *
import numpy as np

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """
    start = np.zeros((2,1))
    goal = np.zeros((2,1))
    maze = 0
    maze_cost = 0

    def __init__(self, start_in , goal_in,maze,maze_cost):
        self.start = start_in
        self.goal = goal_in
        self.maze = maze
        self.maze_cost = maze_cost

    def getStartState(self):
        """
            Returns the start state for the search problem.
        """
        return self.start

    def isGoalState(self, state):
        """ state: Search state
            Returns True if and only if the state is a valid goal state.
        """
        result = False
        if np.array_equal(self.goal,state) == True:
            result = True
        return result

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        successor = []
        action = []
        stepCost = []
        tempa = 0
        tempb = 0
        if state[1] - 1 >= 0:
            if self.maze[state[1]-1 ,state[0]] == 0:
                tempa = state[1] - 1
                tempb = state[0]
                successor.append([tempb,tempa])
                stepCost.append(self.maze_cost[tempa,tempb])
                action.append('N')
        if state[1] + 1 < 30:
            if self.maze[state[1]+1 ,state[0]] == 0:
                tempa = state[1] + 1
                tempb = state[0]
                successor.append([tempb,tempa])
                stepCost.append(self.maze_cost[tempa,tempb])
                action.append('S')
        if state[0] - 1 >= 0:
            if self.maze[state[1] ,state[0]-1] == 0:
                tempa = state[1]
                tempb = state[0] - 1
                successor.append([tempb,tempa])
                stepCost.append(self.maze_cost[tempa,tempb])
                action.append('W')
        if state[0] + 1 < 30:
            if self.maze[state[1] ,state[0]+1] == 0:
                tempa = state[1]
                tempb = state[0] + 1
                successor.append([tempb,tempa])
                stepCost.append(self.maze_cost[tempa,tempb])
                action.append('E')
        return successor,action,stepCost

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        x = self.start[0]
        y = self.start[1]
        cost = 0
        for i in actions:
            if i == 'W':
                x = x-1
            elif i == 'E':
                x = x+1
            elif i == 'N':
                y = y-1
            elif i == 'S':
                y = y+1
            cost = cost + self.maze_cost[y,x]
        return cost

def general_ui_search(problem, fringe):

    cost=[]
    start, goal,maze,maze_cost = problem
    Agente = SearchProblem(start,goal,maze,maze_cost)

    visited = util.Stack()
	#fringe = Queue()    #LIFO
    fringe.push((start,[]))

    while True:
        current , actions = fringe.pop()
		#print(current)

        if Agente.isGoalState(current):
            print("Goal :)	The accions are:")
            print(actions)
            cost = Agente.getCostOfActions(actions)
            print("\nCost : %s Steps" % (cost))
            break
        if current not in visited.get_list():
            sucesores,accion,costo = Agente.getSuccessors(current)
            for i in range(len(sucesores)):
                if not sucesores[i] in visited.get_list():
                    fringe.push((sucesores[i], actions + [accion[i]]))
        visited.push(current)
    return visited.get_list() , actions , cost

def general_search(problem, frontier):
    cost = 0
    start, goal,maze,maze_cost = problem
    Agente = SearchProblem(start,goal,maze,maze_cost)

    visited = util.Stack()
    item = start,[]
    prior = 0
    fringe = frontier
    fringe.push((item),prior)

    while True:
        current , actions = fringe.pop()

        if Agente.isGoalState(current):
            print("Goal :)	The accions are:")
            print(actions)
            cost = Agente.getCostOfActions(actions)
            print("\nCost : %s Steps" % (cost))
            break
        if current not in visited.get_list():
            sucesores,accion,costo = Agente.getSuccessors(current)
            for i in range(len(sucesores)):
                if not sucesores[i] in visited.get_list():
                    item = sucesores[i], actions + [accion[i]]
                    prior = Agente.getCostOfActions(actions) + costo[i]
                    fringe.push((item),prior)
        visited.push(current)
    return visited.get_list() , actions , cost

def depthFirstSearch(problem):
        """
        Search the deepest nodes in the search tree first.

        Your search algorithm needs to return a list of actions that reaches the
        goal. Make sure to implement a graph search algorithm.

        To get started, you might want to try some of these simple commands to
        understand the search problem that is being passed in:

        print "Start:", problem.getStartState()
        print "Is the start a goal?", problem.isGoalState(problem.getStartState())
        print "Start's successors:", problem.getSuccessors(problem.getStartState())
        """
        "*** YOUR CODE HERE ***"
        visited , accions , costs = general_ui_search(problem, util.Stack())
        return visited , accions , costs

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return general_ui_search(problem, util.Queue())

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited , actions , cost = general_search(problem, util.PriorityQueue())
    return visited , actions , cost

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
