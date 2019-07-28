n,k=input().split()
n=int(n)
k=int(k)
count=0
l=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if(abs(l[i]-l[j])==k):
            count+=1
print(count)
