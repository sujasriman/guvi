N=int(input())
K=int(input())
s=0
if(N>0):
    for i in range(1,K+1):
        s=s+i
    print(s)
else:
    print("invalid")
