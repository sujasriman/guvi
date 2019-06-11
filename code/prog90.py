string=input()
string1=''
for i in range(len(string)):
    if(string[i].isdigit()):
        string1=string1+string[i]
print(string1)
