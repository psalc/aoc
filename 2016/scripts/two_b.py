from two_a import lines
from typing import Tuple, List

number_pad = {
    (2, 0): 'D',
    (1, 1): 'A',
    (2, 1): 'B',
    (3, 1): 'C',
    (0, 2): '5',
    (1, 2): '6',
    (2, 2): '7', 
    (3, 2): '8',
    (4, 2): '9',
    (1, 3): '2',
    (2, 3): '3',
    (3, 3): '4',
    (2, 4): '1'
}

def parse_line(line: List[str], starting_pos: Tuple[int, int]) -> Tuple[Tuple[int, int], str]:
    x, y = starting_pos
    valid_pos = number_pad.keys()

    for step in line:
        if step == 'L' and (x-1, y) in valid_pos:
            x -= 1
        if step == 'R' and (x+1, y) in valid_pos:
            x += 1
        if step == 'U' and (x, y+1) in valid_pos:
            y += 1
        if step == 'D' and (x, y-1) in valid_pos:
            y -= 1

    return (x, y), number_pad[(x, y)]

def main():
    code = []
    starting_pos = (0, 2)
    for line in lines:
        starting_pos, digit = parse_line(line, starting_pos)
        code.append(digit)
    print(code)

if __name__ == "__main__":
    main()