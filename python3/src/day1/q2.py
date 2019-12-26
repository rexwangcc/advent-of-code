import math
from typing import Union
from pathlib import Path


def get_fuel_recur(mass: Union[str, int]) -> int:
    """Find the fuel required for a module. Recurrsively
    compute the fuel until it's zero or negative."""
    if int(mass) <= 0:
        return 0
    fuel = math.floor(int(mass) / 3) - 2
    return get_fuel_recur(fuel) + fuel if fuel > 0 else 0


if __name__ == "__main__":
    inputs_path = Path(__file__).parents[0] / "q1.txt"
    with inputs_path.open(mode="r") as fp:
        inputs = fp.readlines()
    print(f"Answer is {sum([get_fuel_recur(x) for x in inputs])}")
