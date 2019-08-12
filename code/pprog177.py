l=list(map(str,input().split()))
for i in range(len(l)-1):
    l1=[]
    for j in range(len(l[i])):
        l1.append(l[i][j])
    l1.sort()
    print(''.join(l1),end=' ')
l1=[]
for i in range(len(l[len(l)-1])):
    l1.append(l[len(l)-1][i])
l1.sort()
print(''.join(l1))
