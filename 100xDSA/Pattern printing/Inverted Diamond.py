n = int(input())

for i in range(n, 0,-1):
    print(f"{'*'*i}{(' '*(n-i))} " , end="")
    print(f"{(' '*(n-i))}{("*"*i)}")

for i in range(2,n+1):
    print(f"{'*'*i}{(' '*(n-i))} " , end="")
    print(f"{(' '*(n-i))}{("*"*i)}")

