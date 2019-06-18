def area(b,h):
    a=(1/2)*b*h
    if(b%2==0 or h%2==0):
        print(int(a))
    else:
        print(a)
b,h=input().split()
b=int(b)
h=int(h)
area(b,h)
