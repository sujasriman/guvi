n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    if(i==l[i]):
        l1.append(l[i])
if(len(l1)==0):
    print(-1)
else:
    for i in range(len(l1)-1):
        print(l1[i],end=' ')
    print(l1[len(l1)-1])
