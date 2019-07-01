n,k=input().split()
n=int(n)
k=int(k)
l1=[]
l=list(map(int,input().split()))
for i in range(n):
    if(l.count(l[i])==k):
        l1.append(l[i])
print(l1[0])
