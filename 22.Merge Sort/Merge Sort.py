nums = [4, 1,8,8,7, 6, 3, 2, 8, 5, 9, 10, 11, 12, 13, 14, 15 , 0,2,2,4,5,7,9]

# first i have to make a function to merge the two sorted arrays

def merge(left, right):
    result = []

    i ,j = 0 , 0
    n , m = len(left) , len(right)

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j += 1
    if i < n:
        while i < n:
            result.append(left[i])
            i += 1
    if (j < m):
        while j < m:
            result.append(right[j])
            j += 1
    return result


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2

    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge(left , right)

print(merge_sort(nums))