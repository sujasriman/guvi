num=int(input())
p=1
while(num>0):
    rem=num%10
    p=p*rem
    num=num/10
    num=int(num)
print(p)
