n,k=input().split()
n=int(n)
k=int(k)
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    if(l[i]<k):
        l1.append(l[i])
l1.sort()
if(len(l1)==1):
    print(l1[0])
else:
    for i in range(len(l1)-1):
        print(l1[i],end=' ')
    print(l1[len(l1)-1])
