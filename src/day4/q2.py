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
