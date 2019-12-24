"""
--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle input is still 138307-654504.
"""
from collections import Counter


def is_valid(password: int) -> bool:
    """Bake the validation rules into the function."""
    str_pwd = str(password)
    candidate = int(str_pwd[0])
    same_adjacent = False
    for i in range(1, len(str_pwd)):
        if int(str_pwd[i]) < candidate:
            return False
        if int(str_pwd[i]) == candidate:
            same_adjacent = True
        candidate = int(str_pwd[i])
    return same_adjacent


def is_valid_2(password: int) -> bool:
    """Bake the validation rules for question part2 into the function."""
    mymap = Counter(str(password))
    return 2 in list(mymap.values())

def main():
    answer_pool = set([])
    # rule 1 & 2: 6-digit within range
    for i in range(138307, 654504 + 1):
        if is_valid(i):
            answer_pool.add(i)
    answer_pool2 = set([])
    for i in answer_pool:
        if is_valid_2(i): answer_pool2.add(i)
    print(f"Answer is {len(answer_pool2)}")

if __name__ == "__main__":
    main()
