def binary_search(arr, l, r, x):

    while l<= r:
        mid = int((l+r)/2)
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binary_search(arr, l, mid-1, x)
        elif x > arr[mid]:
            return binary_search(arr, mid+1, len(arr)-1, x)
    return -1

arr = [10,20,30,40,50,60,70,80,90]
x = int(input("Enter the number you want to search "))

result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
    print(f'the number is at position {result}')
else:
    print("number not found")
