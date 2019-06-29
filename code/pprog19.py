n=int(input())
l=[]
l1=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
for i in range(1,len(l)):
    count=0
    for j in range(1,l[i]+1):
        if(l[i]%j==0):
            count+=1
    if(count==2):
        l1.append(l[i])
if(len(l1)==1):
    print(l1[0])
else:
    for i in range(len(l1)-1):
        print(l1[i],end=' ')
    print(l1[len(l1)-1])
