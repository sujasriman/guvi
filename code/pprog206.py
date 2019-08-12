s=input()
l=[]
count=0
for i in range(len(s)):
    l.append(s[i])
for i in range(len(l)):
    a=ord(l[i])
    if((a>=65 and a<=70)or(a>=48 and a<=57)):
        count+=1
if(count==len(s)):
    print('yes')
else:
    print('no')
