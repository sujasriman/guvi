string=input()
count=0
for i in range(len(string)):
    if(string[i].isalnum()):
        count+=1
print(len(string)-count)
