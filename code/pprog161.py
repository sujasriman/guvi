def isvowel(a):
  if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U'):
    return 1
  else:
    return 0
n=int(input())
l=[]
count=0
for i in range(n):
    s=input()
    l.append(s)
for i in range(len(l)):
  for j in range(len(l[i])):
    b=isvowel(l[i][j])
    if(b==1):
      count+=1
      break
if(count==n):
    print("yes")
else:
    print("no")
