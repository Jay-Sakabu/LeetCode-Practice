import unittest
from groupAnagrams import Solution

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_case(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = self.solution.groupAnagrams(strs)
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertCountEqual([set(g) for g in result], [set(g) for g in expected])

    def test_empty_list(self):
        strs = []
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, [])

    def test_single_word(self):
        strs = ["abc"]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, [["abc"]])

    def test_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        result = self.solution.groupAnagrams(strs)
        expected = [["abc"], ["def"], ["ghi"]]
        self.assertCountEqual([set(g) for g in result], [set(g) for g in expected])

    def test_all_anagrams(self):
        strs = ["abc", "bca", "cab", "cba", "bac", "acb"]
        result = self.solution.groupAnagrams(strs)
        expected = [["abc", "bca", "cab", "cba", "bac", "acb"]]
        self.assertCountEqual([set(g) for g in result], [set(g) for g in expected])

if __name__ == '__main__':
    unittest.main()