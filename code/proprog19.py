k=int(input())
l1=[]
l=[]
for i in range(k):
    l=list(map(int,input().split()))
    for j in range(len(l)):
        l1.append(l[j])
l1.sort()
for i in range(len(l1)-1):
    print(l1[i],end=' ')
print(l1[len(l1)-1])
