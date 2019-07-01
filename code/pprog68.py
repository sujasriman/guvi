n=int(input())
l1=[]
l=list(map(int,input().split()))
for i in range(n):
    b=l.count(l[i])
    l1.append(b)
print(max(l1))
