string=input()
l=len(string)
string1=''
for i in range(l-1,-1,-1):
    string1+=string[i]
if(string==string1):
    print("yes")
else:
    print("no")
