N=int(input())
l=[int(x) for x in input().split()]
if N>=1 and N<=100000:
    m=sorted(l)
    if N%2!=0:
        n=m[int(N/2)]
    else:
        n=m[int((int(N/2)+int(N/2+1))/2.0)]
        
    
print(n)
