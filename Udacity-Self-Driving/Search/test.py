grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

#%%

def drawpath(path_map,path,goal,init):
    next_ = goal
    while (next_ != init):
        index = path[next_[0]][next_[1]]
        next_[0] -= delta[index][0]
        next_[1] -= delta[index][1]
        path_map[next_[0]][next_[1]] = delta_name[index]
    return path_map

#%%

def findpath(grid,init,goal,cost):
    closed = grid
    path = [[0 for j in grid[0]] for i in grid]
    path_map = [[' ' for col in grid[0]] for row in grid]
    path_map[goal[0]][goal[1]] = '*'
    open_ = [[0]+init]
    grid_height = len(grid)
    grid_width = len(grid[0])
    found = False
    resign = False
    while found == False and resign == False:
        open_.sort(key=lambda x: x[0])
        next_ = open_[0]
        open_.reverse()
        open_.pop()
        if next_[1] == goal[0] and next_[-1] == goal[1]:
            found = True
            path_map = drawpath(path_map,path,goal,init)
            return path_map
        for i,move in enumerate(delta):
            g_ = next_[0]+cost
            y_ = next_[1]+move[0]
            x_ = next_[2]+move[1]
            if 0 <= y_ < grid_height and 0 <= x_ < grid_width and closed[y_][x_]==0:
                open_.append([g_,y_,x_])
                closed[y_][x_] = 1
                path[y_][x_] = i
        if len(open_) == 0:
            resign = True
            print('fail')
            return [-1,-1,-1]
    return path_map

#%%

a = findpath(grid,init,goal,cost)
print(a)