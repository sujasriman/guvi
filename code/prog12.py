a=int(input())
temp=a
b=0
while(a>0):
    rem=a%10
    b=(b*10)+rem
    a=a/10
    a=int(a)
if(b==temp):
    print("yes")
else:
    print("no")
