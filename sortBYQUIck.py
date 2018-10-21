def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first = quicksort(x[:i])
        second = quicksort(x[i+1:])
        first.append(x[i])
        return first + second
        
a = [int(y) for y in input().split()]
quicksort(a)
print(a)
