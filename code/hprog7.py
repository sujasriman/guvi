n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    if(i%2==0):
        if(l[i]%2!=0):
            l1.append(l[i])
    else:
        if(l[i]%2==0):
            l1.append(l[i])
for i in range(len(l1)-1):
    print(l1[i],end=' ')
print(l1[len(l1)-1])
