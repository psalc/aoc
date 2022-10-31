from constants import INPUT_DIR

file = INPUT_DIR + '2.txt'

with open(file, 'r') as f:
    lines = [list(line.strip()) for line in f.readlines()]

def main():
    raise NotImplementedError

if __name__ == "__main__":
    main()