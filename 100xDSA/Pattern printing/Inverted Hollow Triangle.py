n = int(input())

for i in range(n, 0 , -1):

    if i == 1 or i == n:
        print(" " * (n - i) + " ".join(["*"] * i))

    else:
        print(f"{' ' * (n - i)}*{' ' * (2 * i - 3)}*")