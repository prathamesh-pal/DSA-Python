'''Given an integer array nums that does not contain any zeros,
 find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

'''


class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        
        max = -1

        for i in nums:
            if i > max:
                if -i in nums:
                    max = i
                
        return max
            


        