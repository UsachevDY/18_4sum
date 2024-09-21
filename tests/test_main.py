import unittest

from source.main import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0

        expected = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

        solution = Solution()
        result = solution.fourSum(nums, target)
        self.assertEqual(len(result), len(expected))

        for sub_array in result:
            self.assertEqual(sum(sub_array), target)

    def test_2(self):
        nums = [2,2,2,2,2]
        target = 8

        expected = [[2,2,2,2]]

        solution = Solution()
        result = solution.fourSum(nums, target)
        self.assertEqual(len(result), len(expected))

        for sub_array in result:
            self.assertEqual(sum(sub_array), target)

    def test_3(self):
        nums = [-3,-2,-1,0,0,1,2,3]
        target = 0

        expected = [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

        solution = Solution()
        result = solution.fourSum(nums, target)
        self.assertEqual(len(result), len(expected))

        for sub_array in result:
            self.assertEqual(sum(sub_array), target)

    def test_4(self):
        nums = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90]
        target = 200

        # expected = []

        solution = Solution()
        result = solution.fourSum(nums, target)
        # self.assertEqual(len(result), len(expected))

        for sub_array in result:
            self.assertEqual(sum(sub_array), target)

    def test_5(self):
        nums = [-2,-1,-1,1,1,2,2]
        target = 0

        expected = [[-2,-1,1,2],[-1,-1,1,1]]

        solution = Solution()
        result = solution.fourSum(nums, target)
        self.assertEqual(len(result), len(expected))

        for sub_array in result:
            self.assertEqual(sum(sub_array), target)