n=int(input())
l=[]
str1=""
for i in range(1,100):
    if(n%i==0):
        l.append(i)
for j in l:
    print(j,end=" ")

    
