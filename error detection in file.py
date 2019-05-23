# read a file
fvar = open(r'C:\Users\agrashas\Desktop\PYTHON FILES\Python\Sample Input\exception error.txt','r')
data = fvar.readlines()  # convert it into list
fvar.close()
print(data)

# fetch the apt output with exception errors
newdata = [x for x in data if('exception' in x.lower())]
print("\n \n")
print(newdata)

# write the ouput to a file
fvar=open(r'C:\Users\agrashas\Desktop\PYTHON FILES\Python\Sample Input\exception errors 1 output.txt','w')
datafinal = fvar.writelines(newdata)
fvar.close()
print(datafinal)
