import math
n,n1 =[int(i) for i in input().split()]
c=n*n1
i=int(math.sqrt(c))
if (c==i*i):
    print("yes")
else:
    print("no")

