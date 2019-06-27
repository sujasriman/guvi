a,b,f,k=input().split()
a=int(a)
b=int(b)
f=int(f)
k=int(k)
c=b
count=0
if(a<b and a>f):
    for i in range(0,(2*k)):
        c=c-a
        if(c<0):
            c=b
            count+=1
    print(count)
else:
    count=-1
    print(count)
