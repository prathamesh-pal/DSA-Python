nums = [1,2,3,6,7,8,7,6]
# only in python 
n = len(nums)

# nums = nums[-1:] +nums[:n-1]

# print(nums)

# wiout using slicing

temp = nums[n-1]

for i in range(n-2 , -1 , -1):
    nums[i+1] = nums[i]
nums[0] = temp

print(nums)