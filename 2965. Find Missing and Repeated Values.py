
import unittest


class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        """brute force checking all number"""
    n = len(grid)
    nums = [0] * n**2
    for i in range(n):
        for n in grid[i]:
            nums[n-1] += 1
    res = [0]*2
    for i in range(len(nums)):
        if nums[i] == 0:
            res[1] = i+1
        if nums[i]  == 2:
            res[0] = i+1
    return res

    # def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
    #     n = len(grid)
    #     seen = set()
    #     res = [0, (n*n)*((n*n) + 1 ) // 2]
    #     for i in range(n):
    #         for j in range(n):
    #             if grid[i][j] in seen:
    #                 res[0] = grid[i][j]
    #             else:
    #                 seen.add(grid[i][j])
    #                 res[1] -= grid[i][j]
    #     return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [2,4],
            self.sol.findMissingAndRepeatedValues(grid = [[1,3],[2,2]]),
        )

    def testcase2(self):
        self.assertEqual([9,5], self.sol.findMissingAndRepeatedValues(grid = [[9,1,7],[8,9,2],[3,4,6]]))

if __name__ == "__main__":
    unittest.main()
