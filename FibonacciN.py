n=int(input())
n1 = 0
n2 = 1
c = 0
if n==1:
   print(n1)
else:
   while c < n:
       print(n2,end=' ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       c+= 1
