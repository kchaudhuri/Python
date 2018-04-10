def answer(xs):
    total = 1
    listTot = []
    if((len(xs) < 1) or (len(xs) > 50)):
        return str(0)

    for i in range(len(xs)):        
        for j in range(len(xs)-i):
            for k in range(len(xs)):
                total = total * xs[k]
                print j,
            print "-"
   
    
    print listTot
    return str(listTot)

x1 = [2,-3,1,0,-5]
x2 = [2,0,2,2,0]
x3 = [-2,-3,4,-5]
x4 = [0,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5]
x5 = [0,-1,19,0]
x6 = [1,2,3]
print answer(x1)
