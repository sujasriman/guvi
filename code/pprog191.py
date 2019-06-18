n=int(input())
l=[]
l1=[]
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=b
for i in range(n-1,-1,-1):
    c=a[i]
    l1.append(c)
if(l==l1):
    print("yes")
else:
    print("no")
