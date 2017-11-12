binList = []
binary=0
dec=input("enter the decimal > ")
n=0
while ((2**n) < dec):
    n=n+1

msb = n-1
for var in range(msb,0,-1):
    if (dec > (2**var)) or (dec == (2**var)):
        dec = (dec - (2**var))
        print 1
        binary = ((binary + 1) * 10)
        binList.append(1)
    else:
        print 0
        binary = (binary * 10)
        binList.append(0)

final = binary/10
print "the equialent binary is {0}".format(final)
##binList = list(final)
print binList

raw_input()
