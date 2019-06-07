s=input()
for i in range(0,len(s)):
    if s[i]=='/':
        c=int(s[0:i])/int(s[i+1:])
    elif s[i]=='%':
        c=int(s[0:i])%int(s[i+1:])
print(int(c))