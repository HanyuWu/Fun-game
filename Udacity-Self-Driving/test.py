
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



def search(grid,init,goal,cost):
    expand = [[-1 for i in grid[1]] for j in grid]
    expand[init[0]][init[1]] = 0
    closed = grid
    closed[init[0]][init[1]] = 1
    open_ = [[0]+init]
    grid_height = len(grid)
    grid_width = len(grid[0])
    found = False
    resign = False
    counter = 0
    while found == False and resign == False:
        open_.sort(key=lambda x: x[0])
        next_ = open_[0]
        open_.reverse()
        open_.pop()
        for move in delta:
            g_ = next_[0]+cost
            y_ = next_[1]+move[0]
            x_ = next_[2]+move[1]
            if 0 <= y_ < grid_height and 0 <= x_ < grid_width and closed[y_][x_]==0:
                open_.append([g_,y_,x_])
                counter +=1
                expand[y_][x_] = counter
                closed[y_][x_] = 1
        if len(open_) == 0:
            resign = True
            print('fail')
            return expand
    return expand


a = search(grid,init,goal,cost)
print(a)
