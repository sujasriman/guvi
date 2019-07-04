s=input()
l=[]
count=0
for i in range(len(s)):
  l.append(s[i])
for i in range(len(l)):
  if(l[i]=='a' or l[i]=='b'):
    count+=1
if(count>=len(l)-1):
  print("yes")
else:
  print("no")
