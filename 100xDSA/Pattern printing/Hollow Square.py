n = int(input())

m = n 

while n:
    if n == m or n == 1  :
        print("*"*m)
    else :
        print(f"*{" "*(m-2)}*")
    n -= 1