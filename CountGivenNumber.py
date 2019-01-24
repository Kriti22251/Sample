n,a=[int(i) for i in input().split()]
n1=list(map(int,input().split()))
c=0
for i in n1:
    if(i==a):
        c=c+1
print(c)

