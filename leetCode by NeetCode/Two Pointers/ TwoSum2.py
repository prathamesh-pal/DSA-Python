

# for i  in range(len(numbers)):
#     for j in numbers[i:]:
#         if numbers[i]+ j == t:
#             print(T
 
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3]

numbers = [2,3,7,2,3]

target = 6

def Sum(numbers , target):
    L,R = 0, len(numbers)-1

    while L < R :
        sum = numbers[L] + numbers[R]
        if sum == target :
            return([L+1 , R+1])
        if sum < target:
            L += 1
        else:
            R -= 1
    return([])
    
print(Sum(numbers,target))


    


