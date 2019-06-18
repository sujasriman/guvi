s=input()
l=[]
l1=[]
for i in range(len(s)):
    l.append(s[i])
for i in range(len(l)):
    asc=ord(l[i])
    if(asc>=65 and asc<=90):
        l1.append(l[i].lower())
    else:
        l1.append(l[i].upper())
print(''.join(l1))
