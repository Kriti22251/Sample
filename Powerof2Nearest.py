a1=int(input())
res = 0; 
for i in range(a1, 0, -1):
    if ((i & (i - 1)) == 0):
        res=i
        break
print(res)
          
           
    
