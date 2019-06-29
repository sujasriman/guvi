n=int(input())
l1=[]
l=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if(l[i]>l[j]):
            d=l[i]-l[j]
        else:
            d=l[j]-l[i]
        l1.append(d)
print(max(l1))
