import curate
from collections import Counter 

def landing_floor(text: str) -> int:
    """
    Part one solution. Calculates the ending floor based on total counts
    of ascents and descents.
    """
    floors = Counter(text)
    return floors["("] - floors[")"]

def first_basement_entry(text: str) -> int:
    """
    Part two solution. Finds the first step where Santa enters basement/level -1
    by iterating over characters and incrementing Santa's current floor.
    """
    current_floor = 0
    position = 0
    map = {"(": 1, ")": -1}
    floors = iter(text)

    while current_floor > -1:
        position += 1
        value = next(floors)
        current_floor += map[value]

    return position


def main():
    input = curate.read_input(1)
    print(f"Santa ends up on: {landing_floor(input)}")
    print(f"Santa first enters the basement at position {first_basement_entry(input)}")


if __name__ == "__main__":
    main()