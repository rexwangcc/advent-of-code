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