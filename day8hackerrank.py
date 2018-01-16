# Enter your code here. Read input from STDIN. Print output to STDOUT

num = input()
phoneBook = {}

for i in range(num):
    temp = raw_input().split(" ")
    phoneBook[temp[0]] = temp[1]

count = 0
while count < num:
    search = raw_input() 

    if search is "":
        break
    if search in phoneBook.keys():
        print search + "=" + phoneBook[search]
    else:
        print "Not found"
    count = count + 1
    
