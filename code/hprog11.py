string=input()
l=list(string.split())
l1=''
for i in range(len(l)):
    for j in range(len(l[i])-1,-1,-1):
        l1=l1+l[i][j]
    l1+=' '
print(l1)
