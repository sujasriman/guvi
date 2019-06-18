n=int(input())
l1=[]
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    c=a[i]
    l1.append(c)
if(b==l1):
    print("yes")
else:
    print("no")
