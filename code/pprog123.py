n=int(input())
l=[]
for i in range(1,n+1):
    count=0
    if(n%i==0):
        for j in range(1,i+1):
            if(i%j==0):
                count+=1
        if(count==2):
            l.append(i)
if(len(l)==1):
    print(l[0])
else:
    for i in range(len(l)-1):
        print(l[i],end=' ')
    print(l[len(l)-1])
