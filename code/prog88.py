N,M=input().split()
N=int(N)
M=int(M)
m=0
if(N>M):
    m=N
else:
    m=M
while(True):
    if(m%N==0 and m%M==0):
        print(m)
        break
    m+=1
