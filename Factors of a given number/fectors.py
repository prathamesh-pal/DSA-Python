from math import sqrt

num = 25 ;

fectors = []

for i in range(1, int(sqrt(num))+1):
    if num%i == 0:
        fectors.append(i)

        if num//i != i :
            fectors.append(num//i) 


print(fectors)