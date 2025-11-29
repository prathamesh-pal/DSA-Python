nums = [1,2,3,4,5,6,0,6,7,7,8,9,9]


def is_sorted(nums):
    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            return False
    return True

print(is_sorted(nums))