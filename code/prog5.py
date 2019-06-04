a,b,c=input().split(" ")
a=float(a)
b=float(b)
c=float(c)
if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
else:
    print(c)
