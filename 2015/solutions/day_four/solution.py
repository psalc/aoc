import curate
from hashlib import md5

def validate_key(hash: str) -> bool:
    if hash.startswith("00000"):
        return True
    return False

def get_hex_value(secret_key: str, number: int) -> str:
    concat = secret_key + str(number)
    return md5(concat).hexdigest()

def main():
    secret_key = curate.read_input(4)
    print(get_hex_value(secret_key, 1))

if __name__ == "__main__":
    main()