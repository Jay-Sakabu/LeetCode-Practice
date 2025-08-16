import unittest
from dupe import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_contains_duplicate_true(self):
        nums = [1, 2, 3, 1]
        self.assertTrue(self.solution.containsDuplicate(nums))

    def test_contains_duplicate_false(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(self.solution.containsDuplicate(nums))

    def test_empty_list(self):
        nums = []
        self.assertFalse(self.solution.containsDuplicate(nums))

    def test_single_element(self):
        nums = [1]
        self.assertFalse(self.solution.containsDuplicate(nums))

if __name__ == "__main__":
    unittest.main()