c=0
n=int(input())
if(n==1):
    c=1
a=n//2
for i in range(a):
    if(n==2**i):
        c+=1
        break
if(c==1):
    print("yes")
else:
    print("no")
