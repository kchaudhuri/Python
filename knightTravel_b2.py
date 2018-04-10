mapd = {}
jump = 0
found = None
def answer(src=-1, dest=-1):
    r, c, num = 8, 8, 0
    sr,sc,dr,dc = 0,0,0,0
    grid = []
    subgrid = []
    global mapd
    global found
    global jump
    mapd = {}
    jump = 0
    found = None
    if((0 <= src <=63) and (0 <= dest <=63)):
        
        for i in range(64):
            mapd[i] = 0
    #############
        for i in range(r):
            for j in range(c):
                subgrid.append(num)
                num = num + 1
            grid.append(subgrid)
            subgrid = []
    #print grid

        for i in range(r):
            for j in range(c):
                if grid[i][j] == src:
                    #print "src {} is located at ({})({})".format(src,i,j)
                    sr, sc = i, j
                if grid[i][j] == dest:
                    #print "dest {} is located at ({})({})".format(dest,i,j)
                    dr, dc = i, j
        mapfoo(grid, sr, sc, dr, dc)
        return found
    else:
        return 0
    
def mapfoo(grid, sr, sc, dr, dc):
    #print jump
    jflag = 0
    global mapd
    if (jump == 0):
        move(grid, sr, sc, dr, dc)
        #print jump

    #print mapd
    if (jump > 0):
        while(found == None):
            jflag = jump
            for i in range(8):
                for j in range(8):
                    if(found == None):
                        if(mapd[grid[i][j]] == jflag):
                            move(grid, i, j, dr, dc)
                            #print "jflag {}".format(jflag)
                            #print "skipping {}".format(grid[i][j])
                    else:
                        break
            
            
            

def move(grid, sr, sc, dr, dc):
    global jump
    jump = mapd[grid[sr][sc]] + 1
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
    global jump
    global found
    #print "element {} is located at ({})({})".format(grid[i][j],i,j)
    if(grid[i][j] == grid[dr][dc]):
        #print "element found with {} jump".format(jump)
        found = jump
    if((mapd[grid[i][j]] == 0) or (mapd[grid[i][j]] > jump)):
        mapd[grid[i][j]] = jump
    
    
for i in range(64):
    for j in range(64):
        print "{} to {}  requires {}".format(i,j,answer(i,j))

