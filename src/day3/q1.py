"""
--- Day 3: Crossed Wires ---
The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?

To begin, get your puzzle input.
"""
from typing import List
from typing import Tuple
from typing import Dict
from collections import Counter
from pathlib import Path


# Misunderstood the problem for the first try...
# def move_to_vector(move: str) -> int:
#     """Convert the direction moves to integers-based vector.
#     The rule is,
#     - R and U are treated as positives,
#     - L and D are treated as negatives.
#     """
#     if move.startswith("R") or move.startswith("U"):
#         return int(move[1:])
#     elif move.startswith("L") or move.startswith("D"):
#         return -int(move[1:])


# def calculate_terminal(wire: List[int]) -> Tuple[int, int]:
#     """Given a wire, compute and return the terminal coordinate as a
#     vector."""
#     horizontals = [
#         move for move in wire if move.startswith("R") or move.startswith("L")
#     ]
#     verticals = [move for move in wire if move.startswith("U") or move.startswith("D")]

#     terminal = (
#         sum(map(move_to_vector, horizontals)),
#         sum(map(move_to_vector, verticals)),
#     )
#     return terminal

# Failed for the second try...
# def next_node(ori: Tuple[int, int], move: str) -> Tuple[int, int]:
#     x, y = ori
#     if move.startswith("R"):
#         return (x + int(move[1:]), y)
#     elif move.startswith("L"):
#         return (x - int(move[1:]), y)
#     elif move.startswith("U"):
#         return (x, y + int(move[1:]))
#     elif move.startswith("D"):
#         return (x, y - int(move[1:]))
#     else:
#         raise ValueError(f"Unexpected instruction {move}")


# def wire_footprints(wire: List[int]) -> List[Tuple[int, int]]:
#     footprints = [(0, 0)]
#     for move in wire:
#         footprints.append(next_node(ori=footprints[-1], move=move))
#     return footprints


# def get_intersections(
#     nodes1: List[Tuple[int, int]], nodes2: List[Tuple[int, int]]
# ) -> List[(Tuple[int, int])]:
#     all_nodes = nodes1 + nodes2
#     all_nodes_counter = Counter(all_nodes)
#     return [node for node in all_nodes_counter if all_nodes_counter[node] >= 2]


def next_node(ori: Tuple[int, int], move: str) -> Tuple[int, int]:
    """Follow the move instruction to move to the next node from ori."""
    x, y = ori
    if move.startswith("R"):
        return (x + int(move[1:]), y)
    elif move.startswith("L"):
        return (x - int(move[1:]), y)
    elif move.startswith("U"):
        return (x, y + int(move[1:]))
    elif move.startswith("D"):
        return (x, y - int(move[1:]))
    else:
        raise ValueError(f"Unexpected instruction {move}")


def plot_wire(wire: List[int]) -> Dict[Tuple[int, int], int]:
    """Return a HashMap of node to step, where node is the nodes on the wire,
    step is the total steps the wire takes to get to the node.
    
    TODO: this function is complex, there are more efficient ways to construct
    the map here :)
    """
    mymap = {}
    ori = (0, 0)
    wire_step = 0
    for instruction in wire:
        dest = next_node(ori, instruction)
        dest_x, dest_y = dest
        ori_x, ori_y = ori
        if dest_x != ori_x:
            _step = 1 if dest_x - ori_x >= 0 else -1
            for coord in range(ori_x, dest_x, _step):
                mymap[(coord, ori_y)] = wire_step
                wire_step += 1
        else:
            _step = 1 if dest_y - ori_y >= 0 else -1
            for coord in range(ori_y, dest_y, _step):
                mymap[(ori_x, coord)] = wire_step
                wire_step += 1
        ori = dest
    return mymap
        

def manhattan_distance(
    destination: Tuple[int, int], origin: Tuple[int, int] = (0, 0)
) -> int:
    x1, y1 = origin
    x2, y2 = destination
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    inputs_path = Path(__file__).parents[0] / "q1.txt"
    with inputs_path.open(mode="r") as fp:
        wires = fp.read().splitlines()
    wire_1 = wires[0].split(",")
    wire_2 = wires[1].split(",")
    
    nodes_on_wire1 = plot_wire(wire_1)
    nodes_on_wire2 = plot_wire(wire_2)

    intersections = set(nodes_on_wire1.keys()).intersection(set(nodes_on_wire2.keys()))
    print(f"All intersections {intersections}")
    print(
        f"Answer in a small-> large sorted list is {sorted(list(map(manhattan_distance, intersections)))}"
    )
