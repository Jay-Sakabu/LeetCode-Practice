# This solution simply checks whether the sorted strings s and t are equal to each other

class Solution:
    def isAnagram(self, s, t):
        return (sorted(s) == sorted(t))