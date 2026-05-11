nums = [1,2,2,1,18,9,7,6]
k = 3
n = len(nums)

nums[:] = nums[-k:][::-1] + nums[:n-k]
print(nums)

# in the midle 
def rotate(nums , start , end):
    while start < end:
        nums[start] , nums[end] = nums[end] , nums[start]
        start += 1
        end -= 1

rotate(nums , 1 , 5)
print(nums)