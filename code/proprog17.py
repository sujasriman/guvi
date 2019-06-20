n,q=input().split()
n=int(n)
q=int(q)
count=0
l=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        s=0
        s=l[i]+l[j]
        if(s==q):
            count+=1
            break
if(count==1):
    print("yes")
else:
    print("no")
