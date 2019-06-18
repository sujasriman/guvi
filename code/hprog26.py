n=int(input())
l1=[]
l=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    l1.append(l[i])
for i in range(n):
    if(i!=len(l1)-1):
        print(l1[i],end='->')
    else:
        print(l1[i])
print(l1)
