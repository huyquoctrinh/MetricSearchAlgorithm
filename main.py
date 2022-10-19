from ast import Str
import os
from tabnanny import check
from algo.algo1 import algo1Path
from utils.draw_map import *
from algo.DepthFirstSearch import *
from algo.BreadthFirstSearch import *
from algo.UniformCostSearch import *
from algo.GreedyBestFirstSearch import *
from algo.ASearch import *
from algo.algo1 import *

inputDir = ['input/level_1/input1.txt',
            'input/level_1/input2.txt',
            'input/level_1/input3.txt',
            'input/level_1/input4.txt',
            'input/level_1/input5.txt',
            'input/level_2/input1.txt',
            'input/level_2/input2.txt',
            'input/level_2/input3.txt',
            'input/level_3/input1.txt',
            'input/level_3/input2.txt',
            'input/level_3/input3.txt'
            ]
outputDir = [
    'output/level_1/input1/',
    'output/level_1/input2/',
    'output/level_1/input3/',
    'output/level_1/input4/',
    'output/level_1/input5/',
    'output/level_2/input1/',
    'output/level_2/input2/',
    'output/level_2/input3/',
    'output/level_3/input1/',
    'output/level_3/input2/',
    'output/level_3/input3/'
]

# bombs = [
# (4,4,-100),
# (6,17,-10)
# ]

# # bombs = [
# #     (3, 6, -10),
# # (5, 14, -15),
# # (6, 5 ,-20),
# # (7, 5, -14),
# # ]

# # maze = [
# # "xxxxxxxxxxxxxxxxx xxxxxxxxxxx",
# # "x                           x",
# # "x                           x",
# # "x                           x",
# # "x   +                       x",
# # "x                           x",
# # "x                +          x",
# # "x                           x",
# # "x      xxxxxxxx             x",
# # "x      x      x             x",
# # "x      x      x             x",
# # "x                           x",
# # "x         S                 x",
# # "x                           x",
# # "x                           x",
# # "x                           x",
# # "x                           x",
# # "x                           x",
# # "x                           x",
# # "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]

# # maze = [
# # "xxxxxxxxxxxxxxxxxxxxxx",
# # "x   x   xx xx        x",
# # "      x     xxxxxxxxxx",
# # "x x   +xx  xxxx xxx xx",
# # "x x   x x xx   xxxx  x",
# # "x          xx +xx  x x",
# # "xxxxx+x x      xx  x x",
# # "xxxxx+xxx  x x  xx   x",
# # "x          x x Sx x  x",
# # "xxxxx x  x x x     x x",
# # "xxxxxxxxxxxxxxxxxxxxxx",
# # ]

# # with open('maze.txt', 'r') as f:
# #     nBombs = int(f.readline())
# #     for i in range(nBombs):
# #         x, y, value = [int(x) for x in next(f).split()]
# #         bombs.append((x, y, value))
# #     for line in f.readlines():
# #         maze.append(line)

# level 1

dirType = ['bfs', 'dfs', 'ucs', 'greedyBFS', 'aStar', 'algo1']

def algoSolve(type, output, dir, maze, visited, start, end, rewards=[]):
    bombs = rewards.copy()
    if type == 1:
        path, cost = bfsPath(maze, visited, start, end)
    elif type == 2:
        path, cost = dfsPath(maze, visited, start, end)
    elif type == 3:
        path, cost = ucsPath(maze, start, end)
    elif type == 6:
        path, cost = ucsPath(maze, start, end, rewards)
    elif type == 4:
        path, cost = gbfsPath(maze, visited, start, end)
    elif type == 7:
        path, cost = gbfsPath(maze, visited, start, end, rewards)
    elif type == 5:
        path, cost = aStar(maze, start, end)
    elif type == 8:
        path, cost = aStar(maze, start, end, rewards)
    elif type == 9:
        path, cost = algo1Path(maze, visited, start, end, rewards)
    newDir = output + dir
    if not(os.path.isdir(newDir)):
        os.mkdir(newDir)
    f = open(newDir + '/{}.txt'.format(dir),'w+')  # w : writing mode  /  r : reading mode  /  a  :  appending mode
    f.write(str(cost) if cost != 0 else 'NO')
    f.close()
    visualize_maze(maze, bombs, start, end, newDir + '/{}.jpg'.format(dir), path)

def solve(input, output, level):
    bombs, maze = read_file(input)
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
            if maze[i][j] == "*":
                start = (i, j)
            if (i == 0 or j == 0 or i == mazeRow - 1 or j == mazeCol - 1) and maze[i][j] == " ":
                end = (i, j)
        visited.append(tmp)
    if level == 1:
        for i in range(5):
            algoSolve(i+1, output, dirType[i], maze, deepcopy(visited), deepcopy(start), deepcopy(end))
    elif level == 2:
        for i in range(2, 5):
            algoSolve(i+4, output, dirType[i], maze, visited, start, end, bombs)
    elif level == 3:
        algoSolve(9, output, dirType[5], maze, visited, start, end, bombs)

#create folder

def makeOutputFolder(root,outputDir:str):
    tmp_dir = './{}'.format(root)+'/'
    if (not os.path.isdir(tmp_dir)):
        os.mkdir(tmp_dir)
        # print('root:',tmp_dir)
    list_child = outputDir.split("/")
    for child in list_child:
        tmp_dir = tmp_dir + child +'/'
        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)
            # print(tmp_dir)
            

for dir in outputDir:
    makeOutputFolder('/',dir)

for i in range(len(inputDir)):
    if i < 5:
        solve(inputDir[i], './' + outputDir[i], 1)
    elif i < 8:
        solve(inputDir[i],'./' + outputDir[i], 2)
    elif i < 11:
        solve(inputDir[i],'./' + outputDir[i], 3)
