n=list(map(int,input().split()))
a=n[0]
for i in range(0,len(n)):
    if(n[i]<a):
        a=n[i]
print(a)
