n = int(input())

for i in range(1, n + 1):

    if i == 1 or i == n:
        print(" " * (n - i) + " ".join(["*"] * i))

    else:
        print(f"{' ' * (n - i)}*{' ' * (2 * i - 3)}*")