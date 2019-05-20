var="""
line1
line2
<start>
A
B
C
<end>
line1
line2
<start>
D
E
F
<end>
line1
line2
<start>
G
H
I
<end>
line1
line2
"""

# c=var.count("<start>")
# print(c)
# print("")

i=0
while i < 3:
    res=var.find("<start>",0,len(var))
    res1=var.find("<end>",0,len(var))
    # print(res)
    # print(res1)
    res=res+7
    data=var[res:res1]
    print(data)
    i=i+1
