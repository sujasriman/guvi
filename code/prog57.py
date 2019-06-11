N,K=input().split()
N=int(N)
K=int(K)
count=0
a=list(map(int,input().split()))
for i in range(N):
    if(a[i]==K):
        count+=1
print(count)
