N,A,D=input().split()
N=int(N)
A=int(A)
D=int(D)
s=0
for i in range(N):
    s=s+A
    A=A+D
print(s)
