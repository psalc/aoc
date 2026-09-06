import curate

def move(pos: tuple[int, int], dir: str) -> tuple[int, int]:
    move_map = {
        ">": lambda x, y: (x, y + 1),
        "<": lambda x, y: (x, y - 1),
        "^": lambda x, y: (x - 1, y),
        "v": lambda x, y: (x + 1, y),
    }

    return move_map[dir](*pos)

def lone_santa(path: str):
    current_position = (0, 0)
    houses_visited = {current_position}

    for dir in path:
        new_pos = move(current_position, dir)
        houses_visited.add(new_pos)
        current_position = new_pos

    return houses_visited

def santa_and_robot(path: str):
    santa_position = (0, 0)
    robo_position = (0, 0)
    houses_visited = {santa_position}

    iterator = iter(path)

    for santa, robo in zip(iterator, iterator):
        new_santa = move(santa_position, santa)
        new_robo = move(robo_position, robo)
        houses_visited.update([new_santa, new_robo])
        santa_position = new_santa
        robo_position = new_robo

    return houses_visited


def main():
    path = curate.read_input(3).strip()
    santa_houses = lone_santa(path)
    both_houses = santa_and_robot(path)

    print(f"Santa visited {len(santa_houses)} houses.")
    print(f"Santa & Robo-Santa visited {len(both_houses)} houses.")
        

if __name__ == "__main__":
    main()