n=int(input())
l=list(map(int,input().split()))
count=0
l1=[]
for i in range(n):
    for j in range(i+1,n):
        if(((abs(l[i]))-(abs(l[j])))==0):
            l1.append(l[i])
            l1.append(l[j])
            count+=1
            break
    if(count==1):
        break
print(l1[0],l1[1])
