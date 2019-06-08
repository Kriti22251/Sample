N,K=[int(x) for x in input().split()]
l=list(map(int,input().split()))
c=""
for i in range(len(l)):
    if l[K-1]%2!=0:
        c=l[K-1]
    else:
        K+=1
print(c)