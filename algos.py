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
from node import Node
from eight_puzzle import EightPuzzle


def bfs(problem):
    print("BFS")
    search_start_time = time.time() # Capture the start time of the search

    root_node = Node(problem.initial) # Initialize the root node with the problem's initial state
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0) # Define the goal state
    frontier = deque([root_node]) # Initialize the frontier with the root node
    explored = set() # Initialize the set of explored states
    generated_nodes_count = 0 # Initialize the number of generated nodes

    while frontier:
        if (time.time() - search_start_time) > 900: # Check for timeout (15 minutes)
            return None, generated_nodes_count, 'TLE'

        current_node = frontier.popleft() # Pop the leftmost node from the frontier
        if current_node.state in explored: # Check if the current state has been explored
            continue
        explored.add(current_node.state) # Add the current state to the set of explored states
        generated_nodes_count += 1

        if current_node.state == goal_state: # Check if the current state is the goal state
            return current_node.solution(), generated_nodes_count, time.time() - search_start_time # Return the solution, total nodes generated, and search duration

        for action in problem.actions(current_node.state): # Iterate over the actions in the problem
            next_state = problem.result(current_node.state, action) # Get the next state from the result of the action
            if next_state not in explored:
                frontier.append(Node(next_state, current_node, action)) # Append the new node to the frontier

    return None, generated_nodes_count, time.time() - search_start_time # Return None and the total nodes generated if the search times out


def ids(problem, search_limit=50):
    print("IDS")
    search_start_time = time.time() # Capture the start time of the search
    total_nodes_generated = 0 # Initialize the total nodes generated
    for current_depth in itertools.count(): # Iterate over increasing depths
        if (time.time() - search_start_time) > 900: # Check for timeout (15 minutes)
            return (None, total_nodes_generated, 'TLE') # Return None and the total nodes generated if the search times out
        if current_depth > search_limit: # Check if the current depth exceeds the search limit
            search_duration = time.time() - search_start_time # Calculate the search duration
            return (None, total_nodes_generated, search_duration) # Return None and the total nodes generated if the search limit is exceeded
        depth_search_result, nodes_generated_at_depth = depth_limited_search(problem, current_depth) # Perform depth-limited search
        total_nodes_generated += nodes_generated_at_depth # Update the total nodes generated
        if depth_search_result not in ['cutoff', None]: # Check if the depth search result is a solution
            search_duration = time.time() - search_start_time # Calculate the search duration
            return (depth_search_result, total_nodes_generated, search_duration) # Return the solution, total nodes generated, and search duration
    search_duration = time.time() - search_start_time # Calculate the search duration
    return (None, total_nodes_generated, search_duration) # Return None and the total nodes generated if the search times out

def depth_limited_search(problem, depth_limit): # Depth Limited Search
    root_node = Node(problem.initial) # Initialize the root node with the problem's initial state
    initial_nodes_generated = 0 # Initialize the number of nodes generated
    return helper(root_node, problem, depth_limit, initial_nodes_generated) # Call the helper function to perform depth-limited search

def helper(current_node, problem, depth_limit, nodes_generated): # Helper function for depth-limited search
    if problem.goal_test(current_node.state): # Check if the current state is the goal state
        return current_node, nodes_generated # Return the current node and the number of nodes generated
    elif depth_limit == 0:  # Check if the depth limit has been reached
        return 'cutoff', nodes_generated # Return 'cutoff' and the number of nodes generated
    else:
        has_cutoff_occurred = False # Initialize the flag for cutoff occurrence
        for child_node in current_node.expand(problem): # Expand the current node to get its children
            nodes_generated += 1 # Increment the number of nodes generated
            recursive_result, nodes_generated = helper(child_node, problem, depth_limit - 1, nodes_generated) # Recur to the next depth level
            if recursive_result == 'cutoff': # Check if a cutoff has occurred
                has_cutoff_occurred = True # Set the flag for cutoff occurrence
            elif recursive_result is not None: # Check if a solution has been found
                return recursive_result, nodes_generated # Return the solution and the number of nodes generated
        return ('cutoff' if has_cutoff_occurred else None), nodes_generated # Return 'cutoff' if a cutoff has occurred, None otherwise
    
  
import heapq
import time
from node import Node  

def astar(problem, heuristic_function): # A* Search
    heuristic_name = "heuristic1" if heuristic_function == problem.heuristic1 else \
                     "heuristic2" if heuristic_function == problem.heuristic2 else \
                     "heuristic3"
    print(f"A* {heuristic_name}")

    def f(node):
        """A* evaluation function."""
        return node.path_cost + heuristic_function(node, problem.goal) # f(n) = g(n) + h(n)

    def heuristic3(self, node):
        """Euclidean distance heuristic."""
        state = node.state  # Current state
        goal_state = self.goal  # Use the class's goal state
        euclidean_distance = sum(math.sqrt((state.index(i) % 3 - goal_state.index(i) % 3) ** 2 +
                                        (state.index(i) // 3 - goal_state.index(i) // 3) ** 2)
                                for i in range(1, 9) if i in state)
        return euclidean_distance
    

    search_start_time = time.time() # Capture the start time of the search
    initial_node = Node(problem.initial, None, None, 0) # Create the initial node
    frontier = [(f(initial_node), initial_node)]  # Priority queue with (priority, node) tuples
    visited_states = set()
    generated_nodes_count = 1 # Initialize the number of generated nodes

    while frontier:
        if time.time() - search_start_time > 900: # Check for timeout (15 minutes)
            return None, generated_nodes_count, 'TLE'

        current_priority, current_node = heapq.heappop(frontier) # Pop the node with the lowest f(n) value
        if current_node.state in visited_states:
            continue

        if problem.goal_test(current_node.state):
            return current_node.solution(), generated_nodes_count, time.time() - search_start_time # Return the solution, total nodes generated, and search duration

        visited_states.add(current_node.state)
        for action in problem.actions(current_node.state): # Iterate over the actions in the problem
            child_state = problem.result(current_node.state, action)
            child_node = Node(child_state, current_node, action, current_node.path_cost + 1) # Create a new node for the next state
            if child_state not in visited_states:
                heapq.heappush(frontier, (f(child_node), child_node)) # Push the child node to the frontier
                generated_nodes_count += 1 # Increment the number of generated nodes

    return None, generated_nodes_count, time.time() - search_start_time # Return None and the total nodes generated if the search times out


