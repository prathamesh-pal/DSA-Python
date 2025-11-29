nums = [1,2,3,4,5,6,-7,8,65,-3,-2345,56,77,8,9,-0,1,2,-3,4,-5,6,-7,8,9]

# method 1: 
largest = nums[0]

for i  in range(1, len(nums)):
    largest = max(largest,nums[i])
print(largest)

# method 2:
largest = float("-inf")
for i in range(1, len(nums)):
    largest = max(largest, nums[i])
print(largest)