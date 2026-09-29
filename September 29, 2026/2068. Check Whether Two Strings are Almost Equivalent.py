'''Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.

The frequency of a letter x is the number of times it occurs in the string.

 '''

# solution

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        fre = {}
        fre2 = {}

        for i in set(word1):
            fre[i] = word1.count(i)

        for i in set(word2):
            fre2[i] = word2.count(i)

        for i in set(word1 + word2):
            d = fre.get(i, 0) - fre2.get(i, 0)

            if abs(d) > 3:
                return False

        return True