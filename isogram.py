n=input()
c=[]
for i in n:
    if i not in c:
        c.append(i)
d="".join(map(str,c))
if n==d:
    print('Yes')
else:
    print('No')
