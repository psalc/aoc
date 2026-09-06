from pathlib import Path
import logging

INPUT_DIR = Path(__file__).parent.parent / "inputs"

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def read_input(day: int) -> str:
    filename = INPUT_DIR / f"{day}.txt"
    logger.info(f"Reading {filename}...")
    with open(filename, 'r') as f:
        return f.read()