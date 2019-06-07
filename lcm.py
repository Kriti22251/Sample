n1,n2=[int(x) for x in input().split()]
def gcd(n1,n2):
    while n2>0:
        n1,n2=n2,n1%n2
    return n1
print(int(n1*n2/gcd(n1,n2)))