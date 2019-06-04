a=input()
b=ord(a)
if((b>=97 and b<=122) or (b>=65 and b<=90)):
    if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U'):
        print("Vowel")
    else:
        print("Consonent")
else:
    print("Invalid")
