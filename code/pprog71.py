n=int(input())
l=list(map(int,input().split()))
l.append(-1)
l1=[]
for i in range(n-1):
    l1.append(max(l[i],l[i+1]))
if(n==1):
    print(l[0])
else:
    for i in range(len(l1)-1):
        print(l1[i],end=' ')
    print(l1[len(l1)-1])
