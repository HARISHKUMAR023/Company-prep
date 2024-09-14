def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        if i < j:
            
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    # Place the pivot in its correct position
    temp = arr[low]
    
    arr[low] = arr[j]
    arr[j] = temp

    return j

def quick(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick(arr, low, p - 1)
        quick(arr, p + 1, high)

# Test the function
arr1 = [4, 6, 2, 5, 7, 9, 1, 3]
quick(arr1, 0, len(arr1) - 1)
print(arr1)
