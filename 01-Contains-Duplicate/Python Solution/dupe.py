# This code checks if a list contains duplicate elements.
# Here we take advantage of Python's set data structure, which only stores unique elements
# Thus, if the length of the set created from the list is different from the length of the list, it means there are duplicates.

class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) < len(nums)