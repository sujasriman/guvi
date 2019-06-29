n,m=input().split()
n=int(n)
m=int(m)
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1=l1+l2
l1.sort()
for i in range(n+m-1):
    print(l1[i],end=' ')
print(l1[n+m-1])
