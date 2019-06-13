string=input()
count=0
for i in range(len(string)):
    if(string[i].isnumeric()):
        count+=1
print(count)
