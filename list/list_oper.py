# indexing 
number = [4,3,7,3,2]
print(number[2])
number[2] = 5
print(number[2])

# size
print(len(number))

# Searching
print(2 in number)
print(number.index(2))
print(number.count(7))


# appending 
number.append(8)
print(number)

# insert 
number.insert(6,0)
print(number)

# Removing an element
# pop the last element
number.pop()
# pop the element n
number.pop(5)
print(number)
# by remove remove the first element ocurence 

number.remove(3)
print(number)

# References and copying
