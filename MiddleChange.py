n=list(input())
str1=""
if (len(n)%2==0):
    c=int((len(n))/2)
    d=c-1
    n[c]="*"
    n[d]="*"
    print(str1.join(n))
else:
     c=int((len(n))/2)
     n[c]="*"
     print(str1.join(n))
     
        
    
    
