x,y=[int(i) for i in input().split()]
x = x ^ y
y = x ^ y
x = x ^ y
print(x,y)
