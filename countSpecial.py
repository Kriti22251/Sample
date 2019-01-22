l=input()
c=0
for i in range(0,len(l)):
    if(l[i]=='.' or l[i]=='@' or l[i]=='#' or l[i]=='$' or l[i]=='%' or l[i]=='!'):
        c=c+1
print(c)
