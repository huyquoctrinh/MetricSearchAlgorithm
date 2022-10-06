# a = map(int, input().split())
# sorted(a)

# def minimum_step(arr):
#     return
bombs = []
maze = []
with open('maze.txt', 'r') as f:
    nBombs = int(f.readline())
    for i in range(nBombs):
        x, y, value = [int(x) for x in next(f).split()]
        bombs.append((x, y, value))
    for line in f:
        maze.append(line)
# print(nBombs)
# for i in range(nBombs):
#     print(bombs[i])
# for line in maze:
#     print(line)

