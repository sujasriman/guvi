n,k=input().split()
a=input()
n=int(n)
k=int(k)
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in range(k):
    l1.append(l2[i])
    l3.append(max(l1))
if(len(l3)==1):
    print(l3[0])
else:
    for i in range(k-1):
        print(l3[i],end=' ')
    print(l3[k-1])
