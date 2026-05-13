N = int(input())

nums = list(map(int, input().split()))

positive = 0
negative = 0
even = 0
odd = 0

for i in nums:

    if i > 0:
        positive += 1

    elif i < 0:
        negative += 1

    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(positive)
print(negative)
print(even)
print(odd)