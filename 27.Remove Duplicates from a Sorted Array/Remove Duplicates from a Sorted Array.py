nums = [0,0,1,1,1,2,3,4,4,4,5,6,6,6,7,7,8]


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




# fre = {}
# for i in nums:
#     fre[i] = 0
# j = 0
# for i in fre.keys():
#     nums[j] = i
#     j += 1

# print(j)

def Remove(nums):
    n = len(nums)

    if n == 1:
        return 1
    i = 0
    j = i+1

    while j < n:
        if nums[j] != nums[i]:
            i+=1
            nums[i], nums[j] == nums[j] , nums[i]
        
        j +=1
    return  i+1
        

print(Remove(nums))

