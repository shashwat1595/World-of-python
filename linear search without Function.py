arr= [00, 10, 20, 30, 40, 50, 60, 70, 80]
n=len(arr)
x = int(input("enter the number to be searched  "))
print("")

if x in arr:
    for i in range(0,n):
        if arr[i]==x:
            print(f'number is found at {i}')
        else:
            i=i+1
else:
    print("not found")
