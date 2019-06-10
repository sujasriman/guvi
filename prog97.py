num=int(input())
r=0
while(num>0):
    rem=num%10
    r=(r*10)+rem
    num=num//10
print(r)
