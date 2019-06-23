n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    a=l.count(l[i])
    l1.append(a)
b=max(l1)
print(l[l1.index(b)])
