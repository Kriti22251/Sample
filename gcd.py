n1,n2=[int(x) for x in input().split()]
while n2>0:
    n1,n2=n2,n1%n2
print(n1)
