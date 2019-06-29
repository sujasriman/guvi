n=int(input())
l1=[]
l=list(map(int,input().split()))
l.append(-1)
count=0
for i in range(n):
    j=i+1
    if(l[i]<l[j]):
        count+=1
    else:
        l1.append(count)
        count=0
        continue
b=max(l1)
print(b+1)
