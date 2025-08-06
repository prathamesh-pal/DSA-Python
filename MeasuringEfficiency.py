import random
import time

def Add(numbers):
    sum = (numbers*(numbers-1))//2

    return sum
def dif(numbers):
    return (numbers * (numbers - 1)) // 2 - sum(range(numbers))


random.seed(1337)
numbers = (random.randint(1, 10**6))

start_time = time.time()
result_s = Add(numbers)
result_D = dif(numbers)
end_time = time.time()

print("Number:", numbers)
print("result:", result_s, result_D )  
print("time:", round(end_time - start_time, 2), "s")