n=int(input("enter no"))
s= 0
temp = n
while temp > 0:
   d= temp % 10
   s =s+ d ** 3
   temp=temp//10
if n == s:
   print("yes")
else:
   print("no")
