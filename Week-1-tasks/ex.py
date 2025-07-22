
# nums = [1,2,3,4]
# left = []
# right = [1]*len(nums)
# result = [1]*len(nums)

# # first left
# left_num = 1
# for i in range(len(nums)):
#     left.append(left_num)
#     left_num *= nums[i]

# print(left)

# # right 
# right_num = 1
# for i in range(len(nums) -1,-1,-1):
#     right[i] = right_num
#     right_num *= nums[i]
# print(right)

# for i in range(len(nums)):
#     result[i] = left[i] * right[i]

# print(result)
nums = [1,2,3,4]
right_list = [1]*len(nums)

        # let a right base value first
right_num = 1
for i in range(len(nums)):
    right_list[i] = right_num
    right_num *= nums[i]
print(right_list)
    


