n = int(input())

p = "0"

for i in range(1, n+1):
    print(p[::-1])
    if i%2 == 0:
        p += "0"
    else:
        p += "1"
    
