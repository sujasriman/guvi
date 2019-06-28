def fact(n):
    f=1
    if(n==0):
        f=1
    else:
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
