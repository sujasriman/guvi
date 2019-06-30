n,x=input().split()
n=int(n)
x=int(x)
l1=[]
l=list(map(int,input().split()))
l.append(0)
for i in range(n):
    for j in range(i+1,n):
        s=l[i]+l[j]
        l1.append(s)
if(x in l1):
    print("yes")
else:
    print("no")
