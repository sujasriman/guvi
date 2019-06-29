s=input()
l=[]
for i in range(len(s)):
    if(s[i].isupper()):
        b=s[i].lower()
    else:
        b=s[i].upper()
    l.append(b)
print(''.join(l))
