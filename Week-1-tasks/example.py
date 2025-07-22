
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# m = 1

# for i in range(len(nums)):
#     if not nums[i] == 0:
#         m = m*nums[i]
# for i in range(len(nums)):
#     if 0 not in nums:
#         D = int( m / nums[i])
#         out.append(D)
#     else:
#         if nums[i] == 0:
#             out.append(m)
#         else:
#             out.append(0)

# print(out)

nums = [-1,1,0,-3,3]
left_product = []
right_product = [1] * len(nums)
result = [1] * len(nums)

# Build left_product
left = 1
for i in range(len(nums)):
    left_product.append(left)
    left *= nums[i]

# Build right_product
right = 1
for i in range(len(nums) - 1, -1, -1):
    right_product[i] = right
    right *= nums[i]

# Build result by multiplying left and right products
for i in range(len(nums)):
    result[i] = left_product[i] * right_product[i]

print(result)


