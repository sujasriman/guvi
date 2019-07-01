n,k=input().split()
n=int(n)
k=int(k)
l=list(map(int,input().split()))
for i in range(len(l)-1,len(l)-1-k,-1):
    l.remove(l[i])
if(len(l)==1):
    print(l[0])
else:
    for i in range(len(l)-1):
        print(l[i],end=' ')
    print(l[len(l)-1])
