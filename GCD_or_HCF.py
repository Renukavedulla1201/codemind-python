def gcd(n,m):
    if n<m:
        n,m=m,n
    c=n
    while n>0:
        if n%c==0 and m%c==0:
            return c
        c-=1
n,m=map(int,input().split())
print(gcd(n,m))