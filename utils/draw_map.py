import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os 

def visualize_maze(matrix, bonus, start, end, output, route=None):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
    #1. Define walls and array of direction based on the route
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j]=='x']

    if route:
        direction=[]
        for i in range(1,len(route)):
            if route[i][0]-route[i-1][0]>0:
                direction.append('v') #^
            elif route[i][0]-route[i-1][0]<0:
                direction.append('^') #v        
            elif route[i][1]-route[i-1][1]>0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    #2. Drawing the map
    ax=plt.figure(dpi=100).add_subplot(111)

    for i in ['top','bottom','right','left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls],[-i[0] for i in walls],
                marker='X',s=100,color='black')
    
    plt.scatter([i[1] for i in bonus],[-i[0] for i in bonus],
                marker='P',s=100,color='green')

    plt.scatter(start[1],-start[0],marker='*',
                s=100,color='gold')

    if route:
        for i in range(len(route)-2):
            if abs(route[i+1][1] - route[i][1]) > 1 or abs(route[i+1][0] -route[i][0]) > 1:
                plt.scatter(route[i+1][1],-route[i+1][0], marker="s", color='blue')
                plt.scatter(route[i][1],-route[i][0], marker="s", color='blue')
            else:
                plt.scatter(route[i+1][1],-route[i+1][0], marker=direction[i],color='silver')

    plt.text(end[1],-end[0],'EXIT',color='red',
         horizontalalignment='center',
         verticalalignment='center')
    plt.xticks([])
    plt.yticks([])
    
    plt.savefig(output)
    

def read_file(file_name: str = 'maze.txt'):
    f=open(file_name,'r')
    n_bonus_points = int(next(f)[:-1])
    bonus_points = []
    for i in range(n_bonus_points):
        inS = f.readline()
        arg = inS.split(' ')
        if len(arg) == 3:
            x, y, reward = map(int, arg)
            bonus_points.append((x, y, reward))
        elif len(arg) == 2:
            x, y = map(int, arg)
            bonus_points.append((x, y))
        elif len(arg) == 4:
            x, y, xx, yy = map(int, arg)
            bonus_points.append((x, y, xx, yy))

    text=f.read()
    matrix=[list(i) for i in text.splitlines()]
    f.close()
    return bonus_points, matrix


def drawSample(matrix, route, tele, bonus, start, end):
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j]=='x']
    if route:
        direction=[]
        for i in range(1,len(route)):
            if route[i][0]-route[i-1][0]>0:
                direction.append('v') #^
            elif route[i][0]-route[i-1][0]<0:
                direction.append('^') #v        
            elif route[i][1]-route[i-1][1]>0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    #2. Drawing the map
    ax=plt.figure(dpi=100).add_subplot(111)

    for i in ['top','bottom','right','left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls],[-i[0] for i in walls],
                marker='X',s=100,color='black')
    
    plt.scatter([i[1] for i in bonus],[-i[0] for i in bonus],
                marker='P',s=100,color='green')
    plt.scatter([i[1] for i in tele],[-i[0] for i in tele],
                marker='s',s=100,color='blue')
    plt.scatter([i[3] for i in tele],[-i[2] for i in tele],
                marker='s',s=100,color='blue')
    plt.scatter(start[1],-start[0],marker='*',
                s=100,color='gold')

    if route:
        for i in range(len(route)-2):
            if abs(route[i+1][1] - route[i][1]) > 1 or abs(route[i+1][0] -route[i][0]) > 1:
                plt.scatter(route[i+1][1],-route[i+1][0], marker="s", color='blue')
                plt.scatter(route[i][1],-route[i][0], marker="s", color='blue')
            else:
                plt.scatter(route[i+1][1],-route[i+1][0], marker=direction[i],color='silver')

    plt.text(end[1],-end[0],'EXIT',color='red',
         horizontalalignment='center',
         verticalalignment='center')
    plt.xticks([])
    plt.yticks([])
    plt.show()


# matrix = [
# "xxxxxxxxxxxxxxxxxxxxxx",
# "x   x   xx xx        x",
# "      x     xxxxxxxxxx",
# "x x   xxx  xxxx xxx xx",
# "x x   x x xx   xxxx  x",
# "x          xx +xx  x x",
# "xxxxx+x x      xx  x x",
# "xxxxx+xxx  x x  xx   x",
# "x          x x *x x  x",
# "xxxxx x  x x x     x x",
# "xxxxxxxxxxxxxxxxxxxxxx"
# ]

# bonus = [
#     (5, 14),
#     (6, 5),
#     (7, 5)
# ]
# tele = [
#     (6, 13),
#     (4, 3)
# ]
# start = (8, 15)
# end = (2, 0)
# drawSample(matrix, None, tele, bonus, start, end)