class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        tempArray = []

        for num, i in count.items():
            tempArray.append([i, num])
        tempArray.sort()

        result = []
        while len(result) < k:
            result.append(tempArray.pop()[1])
        return result
