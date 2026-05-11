nums = [2,3,22,1,3,4,5,6,7,8,9,9,0,9,7,6,5,54,4,3,3] ;


fre = {} 

for i in range(0 , len(nums)):
    if nums[i] in fre:
        fre[nums[i]] += 1 
    
    else:
        fre[nums[i]] = 1


freq = {}

for i in nums :
    freq[i] = freq.get(i , 0)+1

print(fre)

print(freq)