n=int(input())
l=list(map(int,input().split()))
s=0
l1=[]
for i in range(n):
    s=s+l[i]
    l1.append(s)
if(len(l1)==1):
    print(l1[0])
else:
    for i in range(len(l1)-1):
        print(l1[i],end=' ')
    print(l1[len(l1)-1])
