from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for string in strs:
            count = [0] * 26  # Assuming only lowercase a-z
            for char in string:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(string)
        return list(result.values())
        