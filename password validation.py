import re

print("enter the password")
print("Note: The password must be 8 letters long containing containing atleast one numeric value and 1 Uppercase letter and 1 special charecter(eg. @,#,$,&,*,_,-)")
pass_create=input("enter value")

while True:
    if (len(pass_create)<8):
        ret=0
        break
    elif not re.findall('[A-Z]',pass_create):
        ret=0
        break
    elif not re.findall('[a-z]',pass_create):
        ret=0
        break
    elif not re.findall('[0-9]',pass_create):
        ret=0
        break
    elif not re.findall('[@:#:$:&:*:_:-]',pass_create):
        ret=0
        break
    else:
        ret=-1
        print("valid password")
        break

if (ret==0):
    print("invalid password")

