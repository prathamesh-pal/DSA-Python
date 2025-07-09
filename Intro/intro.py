
#       Implementing an algorithm
# def count_even1(x):
#     counting = 0
#     for i in x:
#         if i%2 == 0:
#             counting += 1
#     return counting

# def count_even2(x):
#     return sum(i%2==0 for i in x)

# print(count_even1([1, 2, 3]))
# print(count_even1([2, 2, 2, 2, 2])) # 5
# print(count_even1([5, 4, 1, 7, 9, 6])) # 2

# Efficiency of algorithms

def max_diff(numbers):
    numbers = sorted(numbers)
    return numbers[-1] - numbers[0]
