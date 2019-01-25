n=input()
c=0
for i in range(0,len(n)):
    if ((n[i]=='1') or (n[i]=='0')):
        c="yes"
    else:
        c="no"
print(c)
