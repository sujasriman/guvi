n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    if(l.count(l[i])>1):
        l1.append(l[i])
l1=list(set(l1))
if(len(l1)!=0):
    for i in range(len(l1)-1):
        print(l1[i],end=' ')
    print(l1[len(l1)-1])
else:
    print("unique")
