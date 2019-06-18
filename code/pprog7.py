string=input()
l=[]
l1=[]
temp=''
for i in range(len(string)):
    l.append(string[i])
for i in range(0,len(l),2):
    l1.append(string[i+1])
    l1.append(string[i])
print(''.join(l1))
