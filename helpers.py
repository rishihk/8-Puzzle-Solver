# Citations: Aimacode, GitHub. https://github.com/aimacode 

def read_state_from_file(file_path): # Read the state from the file
    with open(file_path, 'r') as file: # Open the file in read mode
        state = [] # Initialize the state list
        for line in file: # Iterate over the lines in the file
            row = line.strip().split() # Split the line by whitespace and remove leading/trailing whitespace
            state.extend(row) # Extend the state list with the elements of the row
    state_with_zero = [0 if x == '_' else int(x) for x in state] # Replace '_' with 0 and convert the elements to integers
    return tuple(state_with_zero) # Return the state as a tuple

def modify_solution_path(solution_list): # Modify the solution path
    path_string = ''.join(solution_list) # Join the solution list to form a string
    translation_table = str.maketrans('UDLR', 'DURL') # Create a translation table to swap U and D, L and R
    return path_string.translate(translation_table) # Return the modified solution path
