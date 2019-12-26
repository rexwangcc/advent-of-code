from pathlib import Path
from typing import Callable, List
from functools import partial
import copy


def dispatch(instruction: str) -> Callable:
    """Return partial-ized function with args baked into the callable."""
    if instruction.startswith("cut"):
        args = instruction.split(" ")[-1]
        return partial(cut_n, int(args))
    elif instruction.startswith("deal with increment"):
        args = instruction.split(" ")[-1]
        return partial(deal_with_increment, int(args))
    elif instruction.startswith("deal into new stack"):
        return deal_into_new_stack


def deal_into_new_stack(cards: List[str]) -> List[str]:
    # == Java-ish old school ==
    # stack = []
    # for i in range(len(cards)):
    #    stack.insert(0, cards.pop(0))
    # return stack

    # == Pythonic way to do this ==
    # Note slicing takes more memory but creates a copy
    # reverse() is more mem-efficient but I want a copy
    return cards[::-1]


def cut_n(n: int, cards: List[str]) -> List[str]:
    # Python supports both pos and neg index slicing :)
    return cards[n:] + cards[0:n]


def deal_with_increment(n: int, cards: List[str]) -> List[str]:
    L = len(cards)
    space = [None] * L

    # == This can be really expensive ==
    # space[0] = cards.pop(0)
    # pointer = n
    # while space[pointer] is None:
    #     space[pointer] = cards.pop(0)
    pointer = 0
    for item in cards:
        space[pointer] = item
        pointer = pointer + n
        if pointer >= L:
            pointer = pointer - L
    return space


def main(inputs: List[str]) -> List[str]:
    """The facade of the program."""
    # Generate the cards
    # Add "c" prefix to the cards to avoid confusion
    cards = [f"c{i}" for i in range(10007)]
    for instruction in inputs:
        cards = dispatch(instruction)(cards)
    for idx, i in enumerate(cards):
        if i == "c2019":
            return idx
    raise ValueError("Something wrong, c2019 is gone ...")


if __name__ == "__main__":
    inputs_path = Path(__file__).parents[0] / "q1.txt"
    with inputs_path.open(mode="r") as fp:
        inputs = [line.strip() for line in fp.readlines()]
    print(f"Answer is {main(inputs)}")
