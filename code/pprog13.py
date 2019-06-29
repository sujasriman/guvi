n=int(input())
s=0
while(n>0):
    rem=n%10
    r=rem*rem
    s=s+r
    n=n//10
print(s)
