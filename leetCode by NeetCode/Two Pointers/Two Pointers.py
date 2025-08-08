
# A phrase is a palindrome 
# if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, 
# it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# s = "A man, a pan, a canal: Panama"

# a = s.casefold()
# S = ""

# for i in a:
#     if i.isalpha():
#             S += i
# if (S[::-1] == S):
#       print(True) 
# else:
#       print(False)

def is_palindrome(s):
    L, R = 0, len(s) - 1
    while L < R:
        if not s[L].isalnum():  # Keep letters and digits only
            L += 1
            continue
        if not s[R].isalnum():
            R -= 1
            continue
        if s[L].casefold() != s[R].casefold():
            return False
        L += 1
        R -= 1
    return True

print(is_palindrome("0P"))  # False now, because '0' != 'P'
print(is_palindrome("0o0")) # True

