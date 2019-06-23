s=input()
l=list(s.split())
a=0
for i in range(len(l)):
    c=0
    for j in range(len(l[i])):
        if(j==0):
            if(l[i][j].isupper()):
                c+=1
        else:
            if(l[i][j].islower()):
                c+=1
    if(c==len(l[i])):
        a+=1
if(a==len(l)):
    print("yes")
else:
    print("no")
