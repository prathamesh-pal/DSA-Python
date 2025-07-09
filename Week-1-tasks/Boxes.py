''' Your task is to pack products into boxes.
    A given maximum number of products fits in each box.
    How many boxes is needed at least?'''

# def minCount(x,y):
#     box = 0
#     while x >= 0:
#         if x > y:
#             x = x-y
#             box += 1
#         elif x <=  y:
#             box += 1
#             break
#     return box

def minCount(total_items, box_capacity):
    return (total_items + box_capacity - 1) // box_capacity  ('''this is called  ceiling division ! 
                                                              This works for positive integers only.''')


print(minCount(100,10))
print(minCount(10, 3)) # 4
print(minCount(10, 4)) # 3
print(minCount(100, 1)) # 100
print(minCount(100, 100)) # 1
print(minCount(100, 99)) # 2
print(minCount(5, 5)) # 1
print(minCount(5, 6)) # 1
        