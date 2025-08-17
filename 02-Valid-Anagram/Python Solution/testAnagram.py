import unittest
from anagram import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def testTrueAnagram(self):
        s = "test"
        t = "sett"
        self.assertTrue(self.solution.isAnagram(s,t))
        
    def testFalseAnagram(self):
        s = "notan"
        t = "anagram"
        self.assertFalse(self.solution.isAnagram(s,t))

if __name__ == "__main__":
    unittest.main()