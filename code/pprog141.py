n=int(input())
l=[]
count=0
for i in range(n):
    st=input()
    l.append(st)
l.append(' ')
for i in range(len(l)-1):
    if(l[i]==l[i+1]):
        count+=1
        break
if(count==1):
    print("yes")
else:
    print("no")
