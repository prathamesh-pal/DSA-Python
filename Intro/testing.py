import random
import time
from intro import max_diff

random.seed(1337)
n = int(input("What is the valu of n:  "))
print("n:", n)
numbers = [random.randint(1, 10**6) for _ in range(n)]

start_time = time.time()
result = max_diff(numbers)
end_time = time.time()
print("result:", result)
print("time:", round(end_time - start_time, 9), "s")
