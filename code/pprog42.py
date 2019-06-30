n=int(input())
count=0
l=list(map(int,input().split()))
l.append(0)
for i in range(n):
    if(l[i]<l[i+1]):
        count+=1
if(count==n-1):
    print("yes")
else:
    print("no")
