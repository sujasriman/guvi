N,M=input().split()
N=int(N)
M=int(M)
p=N*M
count=0
if(p==0):
    count+=1
for i in range(p//2):
    if((i*i)==p):
        count+=1
if(count==1):
    print("yes")
else:
    print("no")
