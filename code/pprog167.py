def p_no(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count==2):
        print('yes')
    else:
        print('no')
l=list(map(str,input().split()))
a=0
for i in range(len(l)):
    a+=len(l[i])
p_no(a)
