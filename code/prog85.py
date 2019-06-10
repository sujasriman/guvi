string=input()
string1=''
string2=''
for i in range(len(string)):
    if(i%2==0):
        string1+=string[i]
    else:
        string2+=string[i]
print(string1,string2)
