n=int(input())
l1=[]
l=list(map(int,input().split()))
for i in range(n):
    if(l[i]<n):
        l1.append(l[i])
if(len(l1)==1):
    print(l1[0])
else:
    for i in range(len(l1)-1):
        print(l1[i],end=' ')
    print(l1[len(l1)-1])
