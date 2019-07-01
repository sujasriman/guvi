n=int(input())
l1=[]
l2=[]
l=list(map(int,input().split()))
for i in range(n):
    l1.append(l[i])
l1.sort()
for i in range(n):
    b=l.index(l1[i])
    l2.append(b+1)
if(len(l2)==1):
    print(l2[0])
else:
    for i in range(len(l2)-1):
        print(l2[i],end=' ')
    print(l2[len(l2)-1])
