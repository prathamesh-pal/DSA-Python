nums = [2, 10, 8]
# self attempted 
def find_second_largest_element(arr):
    largest = float("-inf")
    l = float("-inf")
    for i in range(0 , len(arr)):
        if largest < arr[i]:
            l = largest
            largest  = arr[i] 
        elif arr[i] > l and arr[i] != largest :
                l = arr[i] 
    return l
print(find_second_largest_element(nums))

# methord

def second_largest(arr):
    large = float("-inf")
    s_large = float("-inf")
    n = len(nums)
    for i in range(0 ,n):
        large = max(large ,nums[i])
    
    for i in range(0 ,n):
        if nums[i] > s_large and nums[i] != large:
            s_large = nums[i]
    return s_large

print(second_largest(nums))