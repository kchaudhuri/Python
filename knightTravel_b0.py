mapd = {}
jump = 0
def answer(src=0, dest=0):
    r, c, num = 8, 8, 0
    sr,sc,dr,dc = 0,0,0,0
    grid = []
    subgrid = []
    global mapd
    #############
    for i in range(64):
        mapd[i] = None
    #############
    for i in range(r):
        for j in range(c):
            subgrid.append(num)
            num = num + 1
        grid.append(subgrid)
        subgrid = []
    print grid

    for i in range(r):
        for j in range(c):
            if grid[i][j] == src:
                print "src {} is located at ({})({})".format(src,i,j)
                sr, sc = i, j
            if grid[i][j] == dest:
                print "dest {} is located at ({})({})".format(dest,i,j)
                dr, dc = i, j
    move(grid, sr, sc, dr, dc)
    print mapd

def move(grid, sr, sc, dr, dc):
    global jump
    jump = jump + 1
    up(grid, sr, sc, dr, dc)
    down(grid, sr, sc, dr, dc)
    left(grid, sr, sc, dr, dc)
    right(grid, sr, sc, dr, dc)

def up(grid, sr, sc, dr, dc):
    if((sr >= 2) and (sc >= 1)):
        mv(grid, sr-2, sc-1, dr, dc)
    if((sr >= 2) and (sc <= 6)):
        mv(grid, sr-2, sc+1, dr, dc)
    if((sr >= 1) and (sc >= 2)):
        mv(grid, sr-1, sc-2, dr, dc)
    if((sr >= 1) and (sc <= 5)):
        mv(grid, sr-1, sc+2, dr, dc)

def down(grid, sr, sc, dr, dc):
    if((sr <= 5) and (sc <= 6)):
        mv(grid, sr+2, sc+1, dr, dc)
    if((sr <= 5) and (sc >= 1)):
        mv(grid, sr+2, sc-1, dr, dc)
    if((sr <= 6) and (sc >= 2)):
        mv(grid, sr+1, sc-2, dr, dc)
    if((sr <= 6) and (sc <= 5)):
        mv(grid, sr+1, sc+2, dr, dc)
        
def left(grid, sr, sc, dr, dc):
    if((sr >= 2) and (sc >= 1)):
        mv(grid, sr-2, sc-1, dr, dc)
    if((sr <= 6) and (sc >= 2)):
        mv(grid, sr+1, sc-2, dr, dc)
    if((sr >= 1) and (sc >= 2)):
        mv(grid, sr-1, sc-2, dr, dc)
    if((sr <= 5) and (sc >= 1)):
        mv(grid, sr+2, sc-1, dr, dc)

def right(grid, sr, sc, dr, dc):
    if((sr >= 1) and (sc <= 5)):
        mv(grid, sr-1, sc+2, dr, dc)
    if((sr <= 6) and (sc <= 5)):
        mv(grid, sr+1, sc+2, dr, dc)
    if((sr >= 2) and (sc <= 6)):
        mv(grid, sr-2, sc+1, dr, dc)
    if((sr <= 5) and (sc <= 6)):
        mv(grid, sr+2, sc+1, dr, dc)
        
def mv(grid, i, j, dr, dc):
    global mapd
    print "element {} is located at ({})({})".format(grid[i][j],i,j)
    if((grid[i][j] is not None) and (grid[i][j] < jump)):
        pass
    else:
        mapd[grid[i][j]] = jump
    
for i in range(64):
    answer(i, 9)
#answer(7, 9)
    

