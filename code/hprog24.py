n,k=input().split()
n=int(n)
k=int(k)
l=list(map(int,input().split()))
count=0
for i in range(n):
    for j in range(i+1,n):
        if(l[i]+l[j]==k):
            count+=1
            break
if(count>=1):
    print("YES")
else:
    print("NO")
