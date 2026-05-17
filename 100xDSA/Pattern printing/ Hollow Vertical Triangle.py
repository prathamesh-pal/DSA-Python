n = int(input())

rows = 2 * n - 1

for i in range(rows):
    
    if i < n:
        spaces = i
    else:
        spaces = rows - i - 1

    if spaces == 0:
        print("* ")
    else:
        print("*" + " " * (2 * spaces - 1) + "* ")