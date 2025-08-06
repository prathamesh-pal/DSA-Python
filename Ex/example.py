# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.


# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# class Solution:
#     nums = [2,7,11,15]
#     t = 9
#     def target(nums,t):
#         for i in range(len(nums)):
#             for j in range(i+1 ,len(nums)):
#                 if (nums[i] + nums[j]) == t:

#                     return i , j



# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.


# nums = [1,2,3,4,1]
# def twice(nums):
#     s = set()
#     for i in nums:
#         if i in s:
#             return True
#         s.add(i)
#     return False

# print(twice(nums))

# s = "anagram"
# t = "nagaram"

# s = sorted(s)
# t = sorted(t)

# if s== t:
#     print(True)

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# strs = ["eat","tea","tan","ate","nat","bat"]

# Dict = {}

# for i in strs:
#         key = "".join(sorted(i))
#         if key in Dict:
#             Dict[key].append(i)
#         else:
#               Dict[key] = [i]
# print(list(Dict.values())[::-1])

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# tokens = ["2","1","+","3","*"]

# up = []
# opr = ['+', '-', '*','/']
# for i in range(len(tokens)):
#     if tokens[i] in opr:
#         u = (eval(f"{tokens[i-2]} {tokens[i]} {tokens[i-1]}"))

#         break

# d = 2 
# k = 3
# l = ['+','-']
# print(eval(f"{d} {l[0]} {k}")) 

# def eval_rpn(tokens):
#     stack = []
#     for token in tokens:
#         if token in ['+', '-', '*', '/']:
#             b = stack.pop()
#             a = stack.pop()
#             if token == '+':
#                 stack.append(a + b)
#             elif token == '-':
#                 stack.append(a - b)
#             elif token == '*':
#                 stack.append(a * b)
#             elif token == '/':  # integer division like LeetCode
#                 stack.append(int(a / b))
#         else:
#             stack.append(int(token))
#     return stack[0]

# # Example usage:
# expr = ["4","13","5","/","+"]  # ((2+3) * (5-1)) = 20
# print(eval_rpn(expr))


# Given n pairs of parentheses,
#  write a function to generate all combinations of well-formed parentheses.


# input = "()"

# def valid(input):
#     map = {')':'(',']':'[', '}':'{' }
#     stack = []
#     for i in input:
#         if i in map.values():
#             stack.append(i)
#         elif i in map:
#             if not stack or stack[-1] != map[i]:
#                 return False
#             stack.pop()
#     return(not stack)
    
# print(valid(input))

#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]

# def generateParenthesis(n):
#     res = []

#     def dfs(s, open, close):
#         if len(s) == 2 * n:   # Base case: string is complete
#             res.append(s)
#             return
#         if open < n:          # Add '(' if possible
#             dfs(s + "(", open + 1, close)
#         if close < open:      # Add ')' if valid
#             dfs(s + ")", open, close + 1)

#     dfs("", 0, 0)
#     return res

# print(generateParenthesis(3))


# '''Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get 
# a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.'''

# tem = [73,74,75,71,69,72,76,73]
# # Output: [1,1,4,2,1,1,0,0]



# for i in range(len(tem)):