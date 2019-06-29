n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in range(n):
    if(l[i]%2==0):
        e.append(l[i])
    else:
        o.append(l[i])
if(len(e)==1):
    print(e[0])
else:
    print(o[0])
