def divide_array(numbers,low,high):
    if low<high:
        mid=(low+high)//2
        divide_array(low,mid-1)
    else:
        divide_array(mid+1,high)
        

def merge_array(arr_a,arr_b):
        merged_array=[]
        i=j=0
        while i<len(arr_a) and j<len(arr_b):
            if arr[i]<arr[j]:
                merged_array[k]=arr_a[i]
                i+=1
            else:
                merged_array[k]=arr_b[j]
                j+=1
            k+=1
        merged_array[k:]=arr_a[i:]+arr_b[j:]
        print("Merged array:",merged_array)




    def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge
    return merge(left, right)


# def merge(left, right):
#     result = []
#     i = j = 0

#     # Compare elements from both arrays
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     # Add remaining elements
#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result


# # Example
# arr = [38, 27, 43, 3, 9, 82, 10]

# sorted_arr = merge_sort(arr)

# print(sorted_arr)