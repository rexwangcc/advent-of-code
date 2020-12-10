from config import fname

R = 1
D = 3

fopen = open(fname, 'r')
lines = [i[:-1] for i in fopen.readlines()]

def cal_trees(forest, R, D):
    repeat = len(lines[0])
    depth = len(lines)
    cross = []
    tree = 0
    for i in range(int(depth/D)):
        meet = forest[i*D][i*R % repeat]
        if meet == '#':
            tree += 1
        cross.append(meet)
    print(tree, "".join(cross))
    return tree

print(cal_trees(lines, 1, 1) * cal_trees(lines, 3, 1) * cal_trees(lines, 5, 1) * cal_trees(lines, 7, 1) * cal_trees(lines, 1, 2))
