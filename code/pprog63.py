n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in range(n):
    for j in range(len(l2)):
        if(l1[i]==l2[j]):
            l3.append(l1[i])
            l2.remove(l2[j])
            break
if(len(l3)==1):
    print(l3[0])
else:
    for i in range(len(l3)-1):
        print(l3[i],end=' ')
    print(l3[len(l3)-1])
