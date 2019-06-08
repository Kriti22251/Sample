N,K=[int(x) for x in input().split()]
l=list(map(int,input().split()))
c=""
if l[K-1]!=min(l):
    c=l[K-1]
else:
    K+=1
print(c)