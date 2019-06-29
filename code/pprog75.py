n=int(input())
count=0
l=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if(l[i]<l[j]):
            count+=1
print(count)
