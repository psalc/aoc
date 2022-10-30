# --- Day 1: No Time for a Taxicab ---
from constants import INPUT_DIR
from typing import Tuple, Dict, List, Any

# Read in input
filepath = INPUT_DIR + "1a.txt"

with open(filepath, 'r') as f:
    data = f.read().split(', ')

# First, get the number of blocks away from starting point
# Initiate starting state
state = {
    "facing": "N",
    "coords": [0, 0]
}

def move(state: Dict[str, str or List[int]], direction: str, moves: int) -> Dict[str, Any]:
    '''
    Takes coords, direction and number of moves and returns
    new coordinates.
    '''
    facing = state["facing"]
    coords = state["coords"]

    if direction == "L":
        if facing == "N":
            coords[0] -= moves
            facing = "W"
        elif facing == "S":
            coords[0] += moves
            facing = "E"
        elif facing == "E":
            coords[1] += moves
            facing = "N"
        elif facing == "W":
            coords[1] -= moves
            facing = "S"
    
    elif direction == "R":
        if facing == "N":
            coords[0] += moves
            facing = "E"
        elif facing == "S":
            coords[0] -= moves
            facing = "W"
        elif facing == "E":
            coords[1] -= moves
            facing = "S"
        elif facing == "W":
            coords[1] += moves
            facing = "N"

    return {"facing": facing, "coords": coords}

def split_instruction(instruction: str) -> Tuple[str, int]:
    '''
    Splits instruction from list into
    a direction and number of moves.
    '''
    direction = instruction[0]
    moves = int(instruction[1:])

    return direction, moves

def get_destination(starting_state: Dict[str, str or List[int]], instructions: List[str]) -> Tuple[int, int]:
    '''
    Iterate through instruction list and get the final destination coordinates.
    '''
    current_state = starting_state

    for step in instructions:
        direction, moves = split_instruction(step)
        current_state = move(current_state, direction, moves)

    return current_state["coords"]

def get_manhattan_distance(destination_coords: Tuple[int, int], starting_coords: Tuple[int, int] = (0, 0)) -> int:
    '''Calculate manhattan distance between destination and start'''
    from scipy.spatial.distance import cityblock
    return cityblock(destination_coords, starting_coords)

print(get_manhattan_distance(get_destination(state, data)))