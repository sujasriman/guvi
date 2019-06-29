n=int(input())
l1=[]
l=list(map(int,input().split()))
for i in range(n):
    b=l.count(l[i])
    l1.append(b)
a=l1.index(min(l1))
print(l1[a])
