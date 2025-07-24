# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
# Therefore its length is 4.

nums =[100, 4, 200, 1, 3, 2]


if len(nums) == 0:
    print(0)
else:
    nums = set(nums)
    nums = sorted(nums)

    count = 1
    max_count = 1
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1
    print(max_count)

