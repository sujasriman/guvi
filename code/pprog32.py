n,k=input().split()
n=int(n)
k=int(k)
count=0
l=list(map(int,input().split()))
for i in range(n):
    if(l[i]==k):
        count+=1
        break
if(count==1):
    print("Yes")
else:
    print("No")
