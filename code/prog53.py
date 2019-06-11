num=int(input())
s=0
while(num>0):
    rem=num%10
    s=s+rem
    num=num//10
print(s)
