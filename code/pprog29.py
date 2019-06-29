l,r=input().split()
l=int(l)
r=int(r)
count=0
for i in range(1,r+1):
    a=i*i
    if(a in range(l,r+1)):
        count+=1
print(count)
