from constants import INPUT_DIR
from typing import List, Tuple

file = INPUT_DIR + '2.txt'

with open(file, 'r') as f:
    lines = [list(line.strip()) for line in f.readlines()]

number_pad = {
    (0, 2): 1,
    (1, 2): 2,
    (2, 2): 3,
    (0, 1): 4,
    (1, 1): 5,
    (2, 1): 6,
    (0, 0): 7,
    (1, 0): 8,
    (2, 0): 9
}

def parse_line(line: List[str], starting_position: Tuple[int, int]) -> Tuple[Tuple[int, int], int]:
    x, y = starting_position

    for step in line:
        if step == 'L' and x > 0:
            x -= 1
        if step == 'U' and y < 2:
            y += 1
        if step == 'R' and x < 2:
            x += 1
        if step == 'D' and y > 0:
            y -= 1
    
    return (x, y), number_pad[(x, y)]


def main():
    code = []
    starting_position = (1, 1)
    for line in lines:
        starting_position, digit = parse_line(line, starting_position)
        code.append(digit)
    print(code)

if __name__ == "__main__":
    main()