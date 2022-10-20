import os
import time
from algo.DijkstraPickUpPoint import algo1Path
from algo.BfsWithTeleport import bfsWithTeleportPath
from utils.draw_map import *
from algo.DepthFirstSearch import *
from algo.BreadthFirstSearch import *
from algo.UniformCostSearch import *
from algo.GreedyBestFirstSearch import *
from algo.AStarSearchH1 import *
from algo.AStarSearchH2 import *
from algo.DijkstraPickUpPoint import *

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
            'input/level_3/input3.txt',
            'input/advance/input1.txt',
            'input/advance/input2.txt',
            'input/advance/input3.txt',
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
    'output/level_3/input3/',
    'output/advance/input1/',
    'output/advance/input2/',
    'output/advance/input3/',
]

dirType = ['bfs', 'dfs', 'ucs', 'greedyBFS', 'aStar', 'dijkstraPickUpPoint', 'bfsWithTeleport']

def algoSolve(type, output, dir, maze, visited, start, end, rewards=[]):
    bombs = rewards.copy()
    newDir = output + dir
    if not(os.path.isdir(newDir)):
        os.mkdir(newDir)
    sTime = time.time()
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
        path, cost = aStarh1(maze, start, end)
    elif type == 8:
        path, cost = aStarh1(maze, start, end, rewards)
        f = open(newDir + '/aStar_heuristic_1.txt','w+')  
        f.write(str(cost) if cost != 0 else 'NO')
        f.close()
        visualize_maze(maze, bombs, start, end, newDir + '/aStar_heuristic_1.jpg', path)

        path, cost = aStarh2(maze, start, end, rewards)
        f = open(newDir + '/aStar_heuristic_2.txt','w+')  
        f.write(str(cost) if cost != 0 else 'NO')
        f.close()
        visualize_maze(maze, bombs, start, end, newDir + '/aStar_heuristic_2.jpg', path)
        return
    elif type == 9:
        path, cost = algo1Path(maze, visited, start, end, rewards)
    elif type == 10:
        path, cost = bfsWithTeleportPath(maze, visited, start, end, rewards)
        bombs = []
    eTime = time.time()
    total = eTime - sTime
    f = open(newDir + '/{}.txt'.format(dir),'w+')  
    f.write('{0}\n{1}'.format(str(cost) if cost != 0 else 'NO', total))
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
    elif level == 4:
        algoSolve(10, output, dirType[6], maze, visited, start, end, bombs)


#create folder

def makeOutputFolder(root,outputDir:str):
    tmp_dir = './{}'.format(root)+'/'
    if (not os.path.isdir(tmp_dir)):
        os.mkdir(tmp_dir)
    list_child = outputDir.split("/")
    for child in list_child:
        tmp_dir = tmp_dir + child +'/'
        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)
            

for dir in outputDir:
    makeOutputFolder('/',dir)

for i in range(len(inputDir)):
    if i < 5:
        solve(inputDir[i], './' + outputDir[i], 1)
    elif i < 8:
        solve(inputDir[i],'./' + outputDir[i], 2)
    elif i < 11:
        solve(inputDir[i],'./' + outputDir[i], 3)
    else:
        solve(inputDir[i],'./' + outputDir[i], 4)
