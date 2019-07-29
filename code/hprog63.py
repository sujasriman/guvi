n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(n-1):
    a=l.pop(i)
    l1.append(max(l))
    l.insert(i,0)
l1.append(0)
for i in range(n-1):
    print(l1[i],end=' ')
print(l1[n-1])
