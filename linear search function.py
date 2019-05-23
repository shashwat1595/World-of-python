
def linear_search_fucntion(arr,n,x):
    for i in range(0,n):
        if arr[i]==x:
            return i
    return -1


arr= [00, 10, 20, 30, 40, 50, 60, 70, 80]
n=len(arr)
x = int(input("enter the number to be searched  "))
print("")

result = linear_search_fucntion(arr,n,x)
if (result==-1):
    print('number not found')
else:
    print(f'number is found at {result}')
