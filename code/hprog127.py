s,a=input().split()
l=[]
d=''
if(len(s)<len(a)):
    b=s
    c=a
else:
    b=a
    c=s
for i in range(len(b)):
    d=d+b[i]
    if(d in c):
        l.append(d)
print(l[len(l)-1])
