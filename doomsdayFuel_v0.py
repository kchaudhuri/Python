def answer(m):
    noOfStates = len(m[0])
    terminals = [] #contains the terminals
    totEvents = [] #every index contains the total outcome for correspong state
    #check for terminal states
    for i in range(noOfStates):
        if(all_same(m[i])):
            terminals.append(i)

    print "the terminals are{}".format(terminals) ##

    for j in range(noOfStates):
        if(j in terminals):
            totEvents.append(0)
        else:
            totEvents.append(0)
            for k in range(noOfStates):
                totEvents[j] = totEvents[j] + m[j][k]

    for i in range(noOfStates):
        if (totEvents[i] is 0):
            pass
        else:
            for j in range(noOfStates):
                if m[i][j] is not 0:
                    print "state {} --> state {} has a probability of {}/{}".format(i,j,m[i][j],totEvents[i])
            

    print"for each state the total no of events are {}".format(totEvents) ##


def all_same(items):
    return all(x == items[0] for x in items)

l1 = [[1,2,3],[1,2,0],[0,0,0]]
l2 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
answer(l2)

