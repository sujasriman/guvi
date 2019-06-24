def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b
num1,num2=input().split()
num1=int(num1)
num2=int(num2)
x,y=swap(num1,num2)
print(x,y)
