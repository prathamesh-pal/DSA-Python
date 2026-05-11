# prestoring value into some datastructure like /list/Dictonary/ set and fetching it .

# 1

'''Constraints'''

'''
1) 1<= n[i] <= 10 
2) n can have 10^8 elements
3) m can have 10^8 elements

'''

n = [1,2,1,2,3,4,3,2,5,6,7,8,8,7,6,5,6,5,6,7,8,9,9,0,0,9,7,7,6,6,5];

m = [10,1,21,9,5,6,2,5] 

# Brut
print("------------This is a BrutForce solution ---------------------")

count = 0

for i in m:
    count = 0
    for j in n:
        if (i == j):
            count += 1
    print (f"{i} come in {count} times.") 



# Optimal 
print("---------------------------This is a optimal solution ------------------------ ")

hashList = [0]*11

for num in n:
    hashList[num] += 1

for num in m:
    if num < 1 or num > 10:
        print(f"{num} came's 0 time's .")
    else :
        print(f"{num} came's {hashList[num]} time's .")

# Dictionary Approch 
print("------------------------This is the dictionary approch --------------------")


fre = {}

for i in n:
    fre[i] = fre.get(i,0) + 1

for i in m:
    print(f"{i} came {fre.get(i,0)} times.")


