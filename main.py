# from utils import draw_map 
# from draw_map import *
from utils.draw_map import *
from algo.DepthFirstSearch import *
from algo.BreadthFirstSearch import *
from algo.UniformCostSearch import *
from algo.GreedyBestFirstSearch import *
from algo.ASearch import *
# readfile tips:
# read 1 number in a line: int(fName.readline())
# read many number in a line: [int(x) for x in next(f).split()]


# a = map(int, input().split())
# sorted(a)

# def minimum_step(arr):
#     return


bombs = [
(3, 6, -10),
(5, 14, -15),
(6, 5, -20),
(7, 5, -14)
]
maze = ["xxxxxxxxxxxxxxxxxxxxxx",
"x   x   xx xx        x",
"      x     xxxxxxxxxx",
"x x   +xx  xxxx xxx xx",
"x x   x x xx   xxxx  x",
"x          xx +xx  x x",
"xxxxx+x x      xx  x x",
"xxxxx+xxx  x x  xx   x",
"x          x x Sx x  x",
"xxxxx x  x x x     x x",
"xxxxxxxxxxxxxxxxxxxxxx"]

# with open('maze.txt', 'r') as f:
#     nBombs = int(f.readline())
#     for i in range(nBombs):
#         x, y, value = [int(x) for x in next(f).split()]
#         bombs.append((x, y, value))
#     for line in f.readlines():
#         maze.append(line)
# bombs, maze = read_file()
mazeRow = len(maze)
mazeCol = len(maze[0])
visited = []
start = None
end = None
for i in range(len(maze)):
    tmp = []
    for j in range(len(maze[i])):
        if maze[i][j] == 'x':
            tmp.append(True)
        else:
            tmp.append(False)
        if maze[i][j] == "S":
            start = (i, j)
        if (i == 0 or j == 0 or i == mazeRow - 1 or j == mazeCol - 1) and maze[i][j] == " ":
            end = (i, j)
    visited.append(tmp)
path = a_star_algorithm(maze, start, end, bombs)
visualize_maze(maze, bombs, start, end, path)
