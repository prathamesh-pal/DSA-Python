nums = [1,2,2,3,3,1,2,3,4,9,6,7,8,4,5,5,6,6,6,5,4,3,3,2,2]


'''if the nums is sorted '''
# def indfghj(nums):
#     i = 0
#     j = 0
#     n = len(nums)
#     while j < n:
#         if nums[j] != nums[i]:
#             i +=1
#             nums[i], nums[j] = nums[j], nums[i]
#         j += 1
#     return(i+1)

# print(indfghj(nums))




fre = {}
for i in nums:
    fre[i] = 0
j = 0
for i in fre.keys():
    nums[j] = i
    j += 1

print(j)
