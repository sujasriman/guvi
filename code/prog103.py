s=input()
l=list(s.split())
l1=[]
for i in range(len(l)):
  for j in range(len(l[i])):
    if(j==0):
      l1.append(l[i][j].upper())
    else:
      l1.append(l[i][j])
  if(i!=len(l)):
    l1.append(' ')
print(''.join(l1))
