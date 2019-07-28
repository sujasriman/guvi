n,k=input().split()
n=int(n)
k=int(k)
l=[]
l1=[]
for i in range(n):
    l.append(input().split())
for i in range(k):
    count=0
    for j in range(n):
        if(l[0][i] in l[j]):
            count+=1
    if(count==n):
        l1.append(int(l[0][i]))
l1.sort()
for i in range(len(l1)-1):
    print(l1[i],end=' ')
print(l1[len(l1)-1])
