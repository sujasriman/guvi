n=int(input())
l=list(map(int,input().split()))
l1=[]
a=0
for i in range(len(l)):
    l1.append(l.count(l[i]))
a=l1.index(min(l1))
print(l[a])
