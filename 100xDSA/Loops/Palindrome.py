n = int(input())

original = n
reverse = 0

while n:
    digit = n % 10
    reverse = (reverse * 10) + digit
    n = n // 10

if original == reverse:
    print("YES")
else:
    print("NO")