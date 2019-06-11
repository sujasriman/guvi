N,M=input().split()
N=int(N)
M=int(M)
i=1
while(i<=N and i<=M):
    if(N%i==0 and M%i==0):
        GCD=i
    i+=1
print(GCD)
