import math
string=input()
l=len(string)
li=list(string)
if(l%2==0):
    mid=l//2
    li[mid-1]='*'
    li[mid]='*'
else:
    mid=math.ceil(l/2)
    li[mid-1]='*'
print(''.join(li))
