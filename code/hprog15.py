n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(n-1):
    count=0
    for j in range(i+1,n):
        if(l[i]>l[j]):
            count+=1
        else:
            count=0
            break
    if(count==n-1-i):
        l1.append(l[i])
l1.append(l[len(l)-1])
for i in range(len(l1)-1):
    print(l1[i],end=' ')
print(l1[len(l1)-1])
print(max(l1))
