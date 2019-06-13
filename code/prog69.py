def sub(a,b):
    if(a>b):
        s=a-b
    else:
        s=b-a
    return s
N,M=input().split()
N=int(N)
M=int(M)
a=sub(N,M)
if(a%2==0):
    print("even")
else:
    print("odd")
    
