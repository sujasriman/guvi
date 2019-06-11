num=int(input())
b=[]
while(num>0):
    rem=num%10
    if(rem%2!=0):
        b.append(rem)
    num=num//10
for i in range(len(b)-1,-1,-1):
    print(b[i],end=' ')
