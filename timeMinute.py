t=int(input())
hr=0
if t<60:
    print("0",t)
elif t==60:
    print("1")
else:
    hr=int(t/60)
    t1=int(t%60)
    print(hr,t1)
    
    
