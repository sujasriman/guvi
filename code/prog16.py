N,Q=input().split()
Q=int(Q)
N=int(N)
P=N+1
count=0
for i in range(P,Q):
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        print(i,end=' ')
    count=0
