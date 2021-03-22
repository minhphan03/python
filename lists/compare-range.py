comparelist = input().split() #list to do the comparison

numrange = input().split() #the max and min number

num=[]
numrange=[]

for i in comparelist: #turn strings to int
    num.append(int(i))

for i in numrange:
    therange.append(int(i))

max = therange[1]
min = therange[0]

for i in num:
    if i>= min and i <= max:
        print(i,end=' ')
