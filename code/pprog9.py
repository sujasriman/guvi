l,r=input().split()
l=int(l)
r=int(r)
p=0
for i in range(l,r+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count==2 or count==1):
        p+=1
print(p)
