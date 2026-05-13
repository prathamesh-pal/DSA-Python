n = int(input())

rn = 0

while n :
    ln = n%10
    rn = (rn*10)+ln
    n = n//10

print(rn)
