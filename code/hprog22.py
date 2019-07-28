n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    p=1
    for j in range(n):
        p=p*l[j]
    p=p//l[i]
    l1.append(p)
for i in range(n-1):
    print(l1[i],end=' ')
print(l1[len(l1)-1])
