string=input()
l=len(string)
count=0
for i in range(l):
    if(string[i] in ('a','e','i','o','u')):
        count+=1
if(count>0):
    print("yes")
else:
    print("no")
