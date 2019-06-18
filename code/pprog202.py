import string
s=input()
v=[]
c=[]
l=[]
for i in range(len(s)):
    l.append(s[i])
for i in range(len(l)):
    if(l[i]=='a' or l[i]=='e' or l[i]=='i' or l[i]=='o' or l[i]=='u' or l[i]=='A' or l[i]=='E' or l[i]=='O' or l[i]=='U' or l[i]=='I'):
        v.append(l[i])
    else:
        c.append(l[i])
l1=v+c
print(''.join(l1))
