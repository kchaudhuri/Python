# Python program to check if the input number is prime or not
def answer(num):
    prime = ""
    j=0
    while (len(prime)<(num + 5)):
        if j > 1:
           for i in range(2,j):
               if (j % i) == 0:
                   break
           else:
               prime = prime + str(j)
           
    
        j=j+1
    return(prime[num:num+5])

print(answer(0))

