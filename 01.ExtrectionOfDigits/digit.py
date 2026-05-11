from math import *

n = 345423 


count = 0
print (int(log10(n)+1))

while n > 0:
    last_digit  = n%10
    print(last_digit)
    count += 1
    n = n//10 

print(count)

# timecomplexity : O(log10(n))
# Spacecomplexity : O(1)