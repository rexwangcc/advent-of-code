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
            print(f"Got opcode {opcode}, something went wrong!")  # ignore the errors
        elif opcode == 99:
            return res  # finished, halt
        elif opcode == 2:
            res[out] = res[in_1] * res[in_2]
        else:
            res[out] = res[in_1] + res[in_2]


def exhaustive_attack(integers: List[int]):
    """Using exhaustive attack to find the target pair. This is O(N^2) complex."""
    for noun in range(0, 100):
        for verb in range(0, 100):
            print(f"->Attacking with noun {noun}, verb {verb}")
            reset_integers = deepcopy(integers)
            reset_integers[1], reset_integers[2] = noun, verb
            res = intcode(integers=reset_integers)[0]
            print(f"Got output {res}")
            if res == 19690720:
                return noun, verb
    raise ValueError("No answer found!")


if __name__ == "__main__":
    inputs_path = Path(__file__).parents[0] / "q1.txt"
    with inputs_path.open(mode="r") as fp:
        inputs = [int(i) for i in fp.readline().split(",")]
    noun, verb = exhaustive_attack(inputs)
    print(f"Answer of 100 * noun + verb is {100 * noun + verb}")
