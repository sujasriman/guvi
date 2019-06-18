string=input().split()
l=[]
for i in range(len(string)):
    for j in range(len(string[i])):
        if(j==0):
            l.append(string[i][j].upper())
        else:
            l.append(string[i][j].lower())
    l.append(' ')
print(''.join(l))
