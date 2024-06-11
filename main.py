# Citations: Aimacode, GitHub. https://github.com/aimacode 

import argparse
from helpers import read_state_from_file, modify_solution_path
from algos import EightPuzzle, bfs, ids, astar
from node import Node

def solve_puzzle(fpath, algo): 
    initial_state = read_state_from_file(fpath) # Read the initial state from the file
    problem = EightPuzzle(initial=initial_state) # Create an instance of the EightPuzzle class with the initial state

    if not problem.check_solvability(initial_state): # Check if the puzzle is unsolvable
        print("Puzzle is not solvable.")
        return
    
    heuristic_mapping = {'h1':"heuristic1", 'h2':"heuristic2", 'h3':"heuristic3"}; # Map the heuristic names to the method names

    if algo == 'BFS':
        solution_node, nodes_generated, total_time = bfs(problem)  # Call the bfs function
    elif algo == 'IDS':
        solution_node, nodes_generated, total_time = ids(problem) # Call the ids function
    elif algo in ['h1', 'h2', 'h3']: 
        heuristic_method = getattr(problem, heuristic_mapping[algo])
        solution_node, nodes_generated, total_time = astar(problem, heuristic_method) # Call the astar function
    else:
        print("Invalid algorithm choice.")
        return

    # Modify this section to correctly handle the TLE scenario
    if total_time == 'TLE':
        # If TLE, pass 'TLE' directly to display_solution to trigger the correct handling
        display_solution('TLE', nodes_generated, total_time)
    else:
        # Otherwise, proceed as normal
        display_solution(solution_node, nodes_generated, total_time)

def display_solution(result, nodes_generated, total_time): # Display the solution
    if result == 'TLE': # Directly handle the 'TLE' case
        print("Total nodes generated:", nodes_generated) 
        print("Total time taken: >15 min")
        print("Path length: Timed out")
        print("Path: Timed out")
    elif isinstance(result, Node):
        solution_path = result.solution() # Get the solution path from the result
        print_solution_details(solution_path, nodes_generated, total_time)
    elif isinstance(result, list):
        solution_path = result # If result is already a list (solution path)
        print_solution_details(solution_path, nodes_generated, total_time)
    else:
        print("No solution found.")

def print_solution_details(solution_path, nodes_generated, total_time):
    if solution_path is not None:
        print("Total nodes generated:", nodes_generated)
        print("Total time taken: {:.4f} seconds".format(total_time))
        print("Path length:", len(solution_path))
        print("Path:", modify_solution_path(solution_path))
    else:
        print("No solution found.")


def main():
    parser = argparse.ArgumentParser(description="Solve an 8-puzzle problem with a specified algorithm.") # Create an ArgumentParser object
    parser.add_argument('--fPath', type=str, help='File path of the puzzle state') # Add an argument for the file path
    parser.add_argument('--algo', type=str, choices=['BFS', 'IDS', 'h1', 'h2', 'h3'], help='Algorithm to use for solving the puzzle') # Add an argument for the algorithm
    
    args = parser.parse_args() # Parse the arguments
    
    solve_puzzle(args.fPath, args.algo) # Solve the puzzle with the specified algorithm

if __name__ == "__main__":
    main()
