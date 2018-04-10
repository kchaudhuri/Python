def answer(xs=[0]):
    neg_list = []
    count_neg = 0
    count_zero = 0
    total = 1
    max_neg = 0
    neg_pos = -1

    if((len(xs) < 1) or (len(xs) > 50)):
        return str(0)
    
    for i in range(len(xs)):
        if(xs[i] is 0):
            count_zero = count_zero + 1
        if(xs[i] < 0):
            neg_list.append(1)
            count_neg = count_neg + 1
            if(max_neg == 0):
                max_neg = xs[i]
                neg_pos = i
            if(max_neg < xs[i]):
                max_neg = xs[i]
                neg_pos = i
        else:
            neg_list.append(0)


    if((max(int(s) for s in xs) is 0) and count_neg <= 1):
        return str(0)
        
    for i in range(len(xs)):
        if(xs[i] == 0):
            pass
        elif(xs[i] == 1):
            pass
        else:
            if(1 <= abs(xs[i]) <= 1000):
                if(count_neg == 1):
                    if(count_zero == (len(xs)-2)):
                        total = total * xs[i] * -1
                        #total = 0
                    if((not neg_list[i]) and (count_zero < (len(xs)-2))):
                        total = total * xs[i]
                    if(len(xs)==1):
                        total = total * xs[i]
                elif((count_neg%2 == 1) and (count_neg is not 1)):
                    if(i == neg_pos):
                        pass
                    else:
                        total = total * xs[i]
                else:
                    total = total * xs[i]
    return str (total)

x1 = [2,-3,1,0,-5]
x2 = [2,0,2,2,0]
x3 = [-2,-3,4,-5]
x4 = [0,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5,2,-3,1,0,-5]
x5 = [0, -1]

final = answer(x5)
print "the output is {} \n".format(final)










