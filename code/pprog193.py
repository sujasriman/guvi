def equa(a,b,x):
    y=a*x+b
    return y
a,b,x=input().split()
a=int(a)
b=int(b)
x=int(x)
ans=equa(a,b,x)
print(ans)
