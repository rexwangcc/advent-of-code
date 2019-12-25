from typing import List
from pathlib import Path
from copy import deepcopy


VALID_OPCODES = ("01", "02", "03", "04", "99")
POS_MODE = "0"
IMM_MODE = "1"


def intcode(integers: List[int], user_input: int) -> List[int]:
    """Advanced Intcode program."""
    res = deepcopy(integers)
    cursor_step = 4
    cursor = 0

    while cursor <= len(res):
        try:
            instruction = str(integers[cursor])
            # padding the instruction to 5-digit first
            instruction = "0" * (5 - len(instruction)) + instruction
            a, b, c, d, e = instruction  # also could be a, b, c, *de = instruction
            opcode = d + e
            if opcode not in VALID_OPCODES:
                print(
                    f"Got opcode {opcode}, something went wrong!"
                )  # ignore the errors
            elif opcode == "99":
                return res  # finished, halt
            elif opcode == "02":
                cursor_step = 4
                # param 1
                if c == POS_MODE:
                    param1 = integers[integers[cursor + 1]]
                elif c == IMM_MODE:
                    param1 = integers[cursor + 1]
                # param 2
                if b == POS_MODE:
                    param2 = integers[integers[cursor + 2]]
                elif b == IMM_MODE:
                    param2 = integers[cursor + 2]
                # param 3
                # > parameters that an instruction writes to will never be in immediate mode.
                param3 = integers[integers[cursor + 3]]
                res[param3] = res[param1] * res[param2]
            elif opcode == "01":
                cursor_step = 4
                # param 1
                if c == POS_MODE:
                    param1 = integers[integers[cursor + 1]]
                elif c == IMM_MODE:
                    param1 = integers[cursor + 1]
                # param 2
                if b == POS_MODE:
                    param2 = integers[integers[cursor + 2]]
                elif b == IMM_MODE:
                    param2 = integers[cursor + 2]
                # param 3
                # > parameters that an instruction writes to will never be in immediate mode.
                param3 = integers[integers[cursor + 3]]
                res[param3] = res[param1] + res[param2]
            elif opcode == "03":
                # > parameters that an instruction writes to will never be in immediate mode.
                cursor_step = 2
                # param 1
                param1 = integers[cursor + 1]
                res[param1] = user_input
            elif opcode == "04":
                cursor_step = 2
                # > parameters that an instruction writes to will never be in immediate mode.
                print(f"Output: {integers[integers[cursor + 1]]}")
            cursor = cursor + cursor_step
        except:
            return res


if __name__ == "__main__":
    inputs_path = Path(__file__).parents[0] / "q1.txt"
    with inputs_path.open(mode="r") as fp:
        inputs = [int(i) for i in fp.readline().split(",")]
    # print(intcode(inputs, user_input=1))
    intcode(inputs, user_input=1)
