string=input()
l=string.split()
l=''.join(l)
l1=[]
for i in range(len(l)):
    if(l[i].isalpha()):
        l1.append(l[i].lower())
l1=set(l1)
print(l1)
c=len(l1)
if(c==26):
    print("yes")
else:
    print("no")
