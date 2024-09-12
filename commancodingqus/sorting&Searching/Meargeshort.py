def merge(arr,low,mid,high):
    temp=[]
    left = low 
    right = mid+1
    while left<=mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    # Copy the remaining elements from the left half, if any
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Copy the remaining elements from the right half, if any
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy back the merged elements into the original array
    for i in range(len(temp)):
        arr[low + i] = temp[i]
   

def mergsort(arr,low,high):
    if low >= high : return 
    mid = (low + high)//2
    mergsort(arr,low,mid)
    mergsort(arr,mid+1,high)
    merge(arr,low,mid,high)
arr = [38, 27, 43, 3, 9, 82, 10]
mergsort(arr, 0, len(arr) - 1)
print(arr)   

# def marge(arr, low , mid , high):
#     t=[]
#     left = low
#     right = mid+1
#     while left <= mid and right  <= high :
#         if arr[left]< arr[right]:
#             t.append(arr[left])
#             left+=1
#         else:
#             t.append(arr[right])
#             right+=1
    
#     #reminging element in left 
#     while left <= mid:
#         t.append(arr[left])
#         left+=1
#     while right <= high :
#         t.append(arr[right])
#         right+=1
#     for i in range(len(t)):
#         arr[low + i]=t[i]
        
    

# def main(arr,low , high):
#     if low >= high : return 
#     mid = (low + high)//2
#     main(arr, low , mid)
#     main(arr,mid+1,high)
#     marge(arr,low , mid , high)
    
# arr=[9,5,6,7,3,4]
# main(arr,0,len(arr)-1)
# print(arr)
