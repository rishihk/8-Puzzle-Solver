# Citations: Aimacode, GitHub. https://github.com/aimacode 

import sys
from collections import deque
from queue import PriorityQueue
import argparse
import time
import itertools
import heapq
import math
import os

class EightPuzzle: # Class for the 8-puzzle problem

    def __init__(self, initial, goal=(1,2,3,4,5,6,7,8,0)): # Constructor
        self.initial = initial
        self.goal = goal

    def find_blank_tile(self, state):
        return state.index(0); # Find the index of the blank tile

    def actions(self, state):
        possible_actions = ['U', 'D', 'L', 'R'] # List of possible actions
        blank_tile_index = self.find_blank_tile(state) # Find the index of the blank tile

        if blank_tile_index % 3 == 0:
            possible_actions.remove('L') # Remove the left action if the blank tile is in the leftmost column
        if blank_tile_index < 3:
            possible_actions.remove('U') # Remove the up action if the blank tile is in the top row
        if blank_tile_index % 3 == 2:
            possible_actions.remove('R') # Remove the right action if the blank tile is in the rightmost column
        if blank_tile_index > 5:
            possible_actions.remove('D') # Remove the down action if the blank tile is in the bottom row
        
        return possible_actions # Return the list of possible actions

    def result(self, state, action):
        blank_tile_index = self.find_blank_tile(state) # Find the index of the blank tile
        new_state = list(state) # Convert the state to a list to modify it
        d = {'U': -3, 'D': 3, 'L': -1, 'R': 1} # Dictionary to map actions to their index changes
        neighbor_index = blank_tile_index + d[action] # Get the index of the neighbor tile
        new_state[blank_tile_index], new_state[neighbor_index] = new_state[neighbor_index], new_state[blank_tile_index] # Swap the blank tile with the neighbor tile

        return tuple(new_state) # Return the new state
    
    def goal_test(self, state):
        return state == self.goal # Check if the current state is the goal state

    def path_cost(self, c, state1, action, state2):
        return c + 1 # Return the path cost
    
    def check_solvability(self, state):
        num_inversions = 0 # Initialize the number of inversions
        for i in range(8): # 0 to 7
            for j in range(i+1, 9): # i+1 to 8
                if state[i] > state[j] and state[i] != 0 and state[j] != 0: # Check if the value at index i is greater than the value at index j
                    num_inversions += 1 # Increment the number of inversions
        return num_inversions % 2 == 0 # Return True if the number of inversions is even, False otherwise
            
    def heuristic1(self, node, goal=None):
        """Heuristic function that counts the number of misplaced tiles."""
        # Assuming node.state and self.goal are both tuples of the same length
        return sum(tile != goal_tile and tile != 0 for tile, goal_tile in zip(node.state, self.goal))
    
    def heuristic2(self, node, goal = None):
        """Manhattan distance heuristic."""
        state = node.state  # Current state
        goal_state = self.goal  # Use the class's goal state
        manhattan_distance = sum(abs((state.index(i) % 3) - (goal_state.index(i) % 3)) + 
                                abs((state.index(i) // 3) - (goal_state.index(i) // 3))
                                for i in range(1, 9) if i in state)
        return manhattan_distance # Return the Manhattan distance

    def heuristic3(self, node, goal = None):
        """Euclidean distance heuristic."""
        state = node.state  # Current state
        goal_state = self.goal  # Use the class's goal state
        euclidean_distance = sum(math.sqrt((state.index(i) % 3 - goal_state.index(i) % 3) ** 2 +
                                        (state.index(i) // 3 - goal_state.index(i) // 3) ** 2)
                                for i in range(1, 9) if i in state)
        return euclidean_distance # Return the Euclidean distance

    def value(self, state): # Return the state
        raise NotImplementedError # Raise an error if the method is not implemented
    
    