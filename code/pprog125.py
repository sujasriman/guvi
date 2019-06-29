n=int(input())
count=0
l1=[]
l=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if(l[j]%l[i]==0):
            count+=1
    if(count==len(l)):
        l1.append(l[i])
l1.sort(reverse=True)
print(l1[0])
