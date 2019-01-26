n = int(input())
if n > 1:
    for i in range(2,n):
        if (n%i) == 0:
            print("no")
            break
    else:
        print("yes prime")
elif num == 0 or 1:
    print(n)
else:
    print("yes")

    
