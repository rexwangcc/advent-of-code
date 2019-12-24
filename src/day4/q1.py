"""
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 138307-654504.
"""

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

def main():
    answer_pool = set([])
    # rule 1 & 2: 6-digit within range
    for i in range(138307, 654504 + 1):
        if is_valid(i):
            answer_pool.add(i)
    print(f"Answer is {len(answer_pool)}")

if __name__ == "__main__":
    main()