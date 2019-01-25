a1=int(input())
c=0
for i in range(2,a1):
    if(a1%i==0):
        c="no"
    else:
        c="yes"
print(c)
