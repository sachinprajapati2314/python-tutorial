def binary_search(arr, x, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [3,4,5,6,7,8,9]
x = 5

result = binary_search(arr,x,0,len(arr)-1)

if result != -1:
    print("element = ",result)
else:
    print("not found")