"""
--- Part Two ---
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

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
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?

Although it hasn't changed, you can still get your puzzle input.
"""
from typing import List
from typing import Tuple
from typing import Dict
from collections import Counter
from pathlib import Path


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

    intersections = list(set(nodes_on_wire1.keys()).intersection(set(nodes_on_wire2.keys())))
    sum_of_steps = [nodes_on_wire1[intersection] + nodes_on_wire2[intersection] for intersection in intersections]
    print(f"Answer in a small-> large sorted list is {sorted(sum_of_steps)}")
