a,b=input().split()
a=int(a)
b=int(b)
for i in range(a+1,b):
    temp=i
    s=0
    while(i>0):
        rem=i%10
        s=s+(rem**3)
        i=i/10
        i=int(i)
    if(s==temp):
        print(s,end=' ')
