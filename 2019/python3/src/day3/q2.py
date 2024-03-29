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

    intersections = list(
        set(nodes_on_wire1.keys()).intersection(set(nodes_on_wire2.keys()))
    )
    sum_of_steps = [
        nodes_on_wire1[intersection] + nodes_on_wire2[intersection]
        for intersection in intersections
    ]
    print(f"Answer in a small-> large sorted list is {sorted(sum_of_steps)}")
