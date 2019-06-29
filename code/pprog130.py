n=int(input())
l1=[]
l=list(map(int,input().split()))
for i in range(n):
    s=0
    if(l[i]%2==0):
        for j in range(i+1):
            s=s+l[j]
        l1.append(s)
    else:
        l1.append(l[i])
if(len(l1)==1):
    print(l1[0])
else:
    for i in range(len(l1)-1):
        print(l1[i],end=' ')
    print(l1[len(l)-1])
