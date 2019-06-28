def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
a,b=input().split()
a=int(a)
b=int(b)
a=fact(a)
b=fact(b)
c=a//b
print(c)
