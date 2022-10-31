from constants import INPUT_DIR
from typing import Tuple, List

filepath = INPUT_DIR + '3.txt'

triangles = []

with open(filepath, 'r') as f:
    triangles.extend([tuple(map(int, line.strip().split())) for line in f.readlines()])

def test_triangle(triangle: Tuple[int, int, int]) -> bool:
    a, b, c = triangle
    sides = [a, b, c]
    greatest = sides.pop(sides.index(max(sides)))
    if sum(sides) > greatest:
        return True
    return False

def count_triangles(triangles: List[Tuple[int, int, int]]) -> int:
    test_results = [test_triangle(triangle) for triangle in triangles]
    return sum(test_results)

def main():
    raise NotImplementedError

if __name__ == "__main__":
    print(count_triangles(triangles))