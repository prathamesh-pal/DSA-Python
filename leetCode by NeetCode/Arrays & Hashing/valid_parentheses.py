mapping = {')': '(', ']': '[', '}': '{'}

s = "({[]})"
stack = []

for i in s:
    if i in mapping.values():
        stack.append(i)
    elif i in mapping:
        if not stack or stack[-1] != mapping[i]:
#             print(False)
         stack.pop()

# print(not stack)


# for i in s:
#     if i in mapping:
        