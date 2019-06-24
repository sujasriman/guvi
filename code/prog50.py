n=int(input())
n=n//2
c=0
for i in range(n):
    if(n==2**i):
        c+=1
        break
if(c==1):
    print("yes")
else:
    print("no")
        
