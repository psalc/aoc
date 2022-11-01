from constants import INPUT_DIR
from typing import Tuple, List
from three_a import count_triangles

filepath = INPUT_DIR + '3.txt'

with open(filepath, 'r') as f:
    raw_data = [tuple(map(int, line.strip().split())) for line in f.readlines()]

def reorganize_triangles(raw_data: List[List[str]]) -> List[List[str]]:
    triangles = []
    for a, b, c in grouper(raw_data, 3):
        triangles.extend(list(zip(a, b, c)))
    return triangles

# Recipe from itertools
def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    from itertools import zip_longest
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')

def main():
    raise NotImplementedError

if __name__ == "__main__":
    triangles = reorganize_triangles(raw_data)
    print(count_triangles(triangles))