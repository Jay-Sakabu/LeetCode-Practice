import unittest
from productExceptSelf import Solution

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.example_nums = [1,2,3,4]

    def test_basic(self):
        assert self.solution.naiveProductExceptSelf(self.example_nums) == [24,12,8,6]

    def test_with_zero(self):
        nums = [0,1,2,3]
        assert self.solution.naiveProductExceptSelf(nums) == [6,0,0,0]

    def test_with_multiple_zeros(self):
        nums = [0,1,0,3]
        assert self.solution.naiveProductExceptSelf(nums) == [0,0,0,0]

    def test_negative_numbers(self):
        nums = [-1,2,-3,4]
        assert self.solution.naiveProductExceptSelf(nums) == [-24,12,-8,6]

    def test_single_element(self):
        nums = [5]
        assert self.solution.naiveProductExceptSelf(nums) == [1]

    def test_two_elements(self):
        nums = [2,3]
        assert self.solution.naiveProductExceptSelf(nums) == [3,2]

    def test_all_ones(self):
        nums = [1,1,1,1]
        assert self.solution.naiveProductExceptSelf(nums) == [1,1,1,1]

if __name__ == '__main__':
    unittest.main()