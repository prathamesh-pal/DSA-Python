n, m = map(int, input().split())

o = n
while n:
    if o == n or n < 2:
        print("*"*m)
    else :
        print(f"*{' '*(m-2)}*")

    n -= 1