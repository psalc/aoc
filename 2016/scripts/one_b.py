from one_a import STARTING_STATE, data, move, split_instruction, get_manhattan_distance

def create_path():

    path = []
    current_state = STARTING_STATE.copy()

    for arc in data:
        direction, moves = split_instruction(arc)
        current_coords = current_state["coords"].copy()
        current_state = move(current_state, direction, moves)
        ending_coords = current_state["coords"].copy()
        x1, y1 = current_coords
        x2, y2 = ending_coords
        step = 1 if y1 < y2 or x1 < x2 else -1
        if x1 == x2:
            path.extend([(x1, y) for y in range(y1, y2, step)])
        elif y1 == y2:
            path.extend([(x, y1) for x in range(x1, x2, step)])

    return path

def find_first_duplicate(path):
    visited = []

    while path:
        current = path.pop(0)
        if current in visited:
            return current
        visited.append(current)

def main():
    path = create_path()
    loc = find_first_duplicate(path)
    print(get_manhattan_distance(loc))

if __name__ == "__main__":
    main()