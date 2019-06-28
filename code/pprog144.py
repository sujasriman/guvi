n=int(input())
l=list(map(int,input().split()))
l1=[]
l.append(-1)
for i in range(len(l)-1):
    if(l[i+1]%l[i]==0):
        l1.append(l[i+1])
if(len(l1)==1):
    print(l1[0])
else:
    for i in range(len(l1)-1):
        print(l1[i],end=' ')
    print(l1[len(l1)-1])
