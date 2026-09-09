from aoc import read_input
from hashlib import md5

def validate_key(hash: str, leading_zeroes: int = 5) -> bool:
    if hash.startswith("0" * leading_zeroes):
        return True
    return False

def get_hex_value(secret_key: str, number: int) -> str:
    concat = secret_key + str(number)
    return md5(concat.encode('utf-8')).hexdigest()

def main():
    secret_key = read_input(4)
    num = 1

    while True:
        hex = get_hex_value(secret_key, num)
        if validate_key(hex):
            print(f"The lowest positive number is {num}!")
            break
        num += 1

if __name__ == "__main__":
    main()