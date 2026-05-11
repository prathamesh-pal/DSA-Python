def minmax(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    else:
        min(minmax(nums[:((n/2)+1)]) ,minmax(nums[n/2 :]))

print(minmax([1,3,5,2,4,8,2,2]))