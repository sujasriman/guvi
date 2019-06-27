k=int(input())
l1=[]
for i in range(k):
    l[i]=input().split()
    for j in range(len(l[i])):
        l[i][j]=int(l[i][j])
        l1.append(l[i][j])
l1.sort()
for i in range(len(l1)-1):
    print(l1[i],end=' ')
print(l1[len(l1)-1])
