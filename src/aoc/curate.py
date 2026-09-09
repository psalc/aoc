from pathlib import Path
import logging

PROJECT_DIR = Path(__file__).parent.parent.parent

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def read_input(day: int, year: int = 2015) -> str:
    INPUT_DIR = PROJECT_DIR / str(year) / "inputs"
    filename = INPUT_DIR / f"{day}.txt"
    logger.info(f"Reading {filename}...")
    with open(filename, 'r') as f:
        return f.read()