import math
from typing import Union
from pathlib import Path


def get_fuel(mass: Union[str, int]) -> int:
    """Find the fuel required for a module."""
    return math.floor(int(mass) / 3) - 2


if __name__ == "__main__":
    inputs_path = Path(__file__).parents[0] / "q1.txt"
    with inputs_path.open(mode="r") as fp:
        inputs = fp.readlines()
    print(f"Answer is {sum([get_fuel(x) for x in inputs])}")
