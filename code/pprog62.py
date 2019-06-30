n=int(input())
l=[]
for i in range(1,n):
    if(n%i==0):
        a=n//i
        if(a%2!=0):
            l.append(i)
print(min(l))
