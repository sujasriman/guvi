n,k=input().split()
n=int(n)
k=int(k)
l=list(map(int,input().split()))
count=0
while(l.count(k)>0 and count<l.count(k)):
    l.remove(k)
if(len(l)==0):
    print("empty")
else:
    for i in range(len(l)-1):
        print(l[i],end=' ')
    print(l[len(l)-1])
