from pathlib import Path
from typing import List, Tuple
from itertools import chain
import copy


def draw(matrix):
    """Draw out the matrix with '#' and '.'."""
    canvas = []
    for row in matrix:
        canvas_row = ""
        for item in row:
            if item == 1:
                canvas_row = canvas_row + "#"
            else:
                canvas_row = canvas_row + "."
        canvas.append(canvas_row)
    for row in canvas:
        print(row)


def evolve(x: int, y: int, matrix: List[List[int]], debug: bool = False) -> int:
    """Compute the next iteration's value of the current value.

    Consider 2 neighbors if it's corner, 3 neighbors if it's edge, otherwise
    evalute all 4 direct neighbors. Chose to use try/except over a lot of 
    nested if/else clauses so the code looks not that hedious :( If the exception
    hanlding is too slow, we could also use another alternative, by putting inequation
    to the if conditions.

    Note: Python List supports [-1] as indices! 
    """
    curr = matrix[x][y]
    opposite = int(not curr)
    try:
        neighbor1 = matrix[x + 1][y]
    except IndexError:
        neighbor1 = 0

    try:
        if x - 1 < 0:
            neighbor2 = 0
        else:
            neighbor2 = matrix[x - 1][y]
    except IndexError:
        neighbor2 = 0

    try:
        neighbor3 = matrix[x][y + 1]
    except IndexError:
        neighbor3 = 0

    try:
        if y - 1 < 0:
            neighbor4 = 0
        else:
            neighbor4 = matrix[x][y - 1]
    except IndexError:
        neighbor4 = 0

    if debug:
        print(f"Neighbors: {[neighbor1, neighbor2, neighbor3, neighbor4]}")

    neighbors = sum([neighbor1, neighbor2, neighbor3, neighbor4])
    if curr == 1:
        return curr if neighbors == 1 else opposite
    if curr == 0:
        return opposite if (neighbors == 1 or neighbors == 2) else curr


def construct_matrix(inputs: List[str]) -> List[List[int]]:
    """Construct the matrix with 0 (clean) and 1 (bug) from the inputs."""
    matrix = []
    for row in inputs:
        matrix.append([1 if i == "#" else 0 for i in row])
    return matrix


def tuplerize(matrix: List[List[int]]) -> Tuple[Tuple[int]]:
    """Tuplerize the matrix so it's hashbale."""
    return tuple(tuple(row) for row in matrix)


def compute_biodiversity_rating(matrix: List[List[int]]) -> int:
    """Compute the resulting biodiversity rating based on the current state matrix."""
    flatten_matrix = list(
        chain.from_iterable(matrix)
    )  # 'itertools.chain' object is not subscriptable
    rating_matrix = [flatten_matrix[i] * (2 ** i) for i in range(0, 25)]
    return sum(rating_matrix)


def main(inputs: List[str], debug: bool = False):
    """The facade of the program."""
    matrix = construct_matrix(inputs)
    lookup_set = set([])
    while True:
        if debug:
            draw(matrix)
            print("Current Matrix:")
            print(matrix)
            print()
        # lookup previous states
        tuplerized_marix = tuplerize(matrix)
        if tuplerized_marix in lookup_set:
            return compute_biodiversity_rating(matrix)
        lookup_set.add(tuplerized_marix)

        # compute the next state
        matrix_next_iter = copy.deepcopy(matrix)
        for i in range(5):
            for j in range(5):
                if debug:
                    print(f"Computing at {(i, j)}")
                    matrix_next_iter[i][j] = evolve(i, j, matrix, debug=debug)
                else:
                    matrix_next_iter[i][j] = evolve(i, j, matrix)
        matrix = matrix_next_iter


if __name__ == "__main__":
    inputs_path = Path(__file__).parents[0] / "q1.txt"
    with inputs_path.open(mode="r") as fp:
        inputs = [line.strip() for line in fp.readlines()]
    # Use debug=True to draw out the process
    print(main(inputs, debug=False))
