n=int(input())
count=0
b=0
l=list(map(int,input().split()))
for i in range(n):
    if(l.count(l[i])==1):
        count+=1
        b=l[i]
        break
if(count>0):
    print(b)
