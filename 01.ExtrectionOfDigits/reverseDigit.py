num = 12345432
n = num

reversN = 0

while n > 0 :
    lastDigit = n%10
    reversN = (reversN*10)+lastDigit

    n = n//10

if reversN == num :
    print("It is a palindrom")
else :
    print("This is not a palindrom")

# TimeComplexity : O(log10(n))
# SpaceComplexity : O(1)