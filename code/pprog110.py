n=int(input())
l=list(map(int,input().split()))
s=0
l1=[]
l2=[]
for i in range(n):
    s=s+l[i]
    l1.append(s)
for i in range(n-1,-1,-1):
    l2.append(l1[i])
if(n>1):
    for i in range(len(l1)):
        l1[i]=l1[i]+l2[i]
if(len(l1)==1):
    print(l1[0])
else:
    for i in range(len(l1)-1):
        print(l1[i],end=' ')
    print(l1[len(l1)-1])
