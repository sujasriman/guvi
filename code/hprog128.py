s=input()
l=[]
for i in range(len(s)):
    a=s[i]
    for j in range(i+1,len(s)):
        a=a+s[j]
        b=''
        for k in range(len(a)-1,-1,-1):
            b=b+a[k]
        if(a==b):
            l.append(a)
l.reverse()
for i in range(len(l)):
    print(l[i])
