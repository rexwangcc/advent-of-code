from typing import List
from pathlib import Path
from copy import deepcopy


VALID_OPCODES = (1, 2, 99)


def intcode(integers: List[int]) -> List[int]:
    """Basic Intcode program."""
    res = deepcopy(integers)
    for cursor in range(0, len(integers) - 1, 4):
        opcode, in_1, in_2, out = integers[cursor : cursor + 4]
        if opcode not in VALID_OPCODES:
            raise ValueError(f"Got opcode {opcode}, something went wrong!")
        elif opcode == 99:
            return res  # finished, halt
        elif opcode == 2:
            res[out] = res[in_1] * res[in_2]
        else:
            res[out] = res[in_1] + res[in_2]


if __name__ == "__main__":
    inputs_path = Path(__file__).parents[0] / "q1.txt"
    with inputs_path.open(mode="r") as fp:
        inputs = [int(i) for i in fp.readline().split(",")]

    # Tweak the inputs as the instructions asked
    inputs[1], inputs[2] = 12, 2
    print(f"Answer is {intcode(inputs)}")
