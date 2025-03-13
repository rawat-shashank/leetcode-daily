from typing import List
import unittest


class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        """differnce array - range update in O(1)"""
        n = len(nums)
        totalSum = 0
        k = 0
        diffArray = [0] * (n+1)

        for idx in range(n):

            while totalSum + diffArray[idx] < nums[idx]:
                k += 1

                # all queries are processed
                if k > len(queries):
                    return -1

                left, right, val = queries[k-1]
                # ignore queries below current index
                if right >= idx:
                    diffArray[max(left, idx)] += val
                    diffArray[right + 1] -= val
            totalSum += diffArray[idx]
        return k


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]),
        )

    def testcase2(self):
        self.assertEqual(
            -1,
            self.sol.minZeroArray(nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]),
        )

    def testcase3(self):
        self.assertEqual(
            0,
            self.sol.minZeroArray(nums = [0], queries = [[0,0,2],[0,0,4],[0,0,4],[0,0,3],[0,0,5]]),
        )

    def testcase4(self):
        self.assertEqual(
            3,
            self.sol.minZeroArray(nums = [10], queries = [[0,0,5],[0,0,3],[0,0,2],[0,0,1],[0,0,4],[0,0,1],[0,0,4],[0,0,5],[0,0,3],[0,0,4],[0,0,1]]),
        )

    def testcase5(self):
        self.assertEqual(
            3,
            self.sol.minZeroArray(nums = [0, 8], queries = [[0,1,4],[0,1,1],[0,1,4],[0,1,1],[1,1,5],[0,1,2],[1,1,4],[0,1,1],[1,1,3],[0,0,2],[1,1,3],[1,1,2],[0,1,5],[1,1,2],[1,1,5]]),
        )
        
    def testcase6(self):
        self.assertEqual(
            4,
            self.sol.minZeroArray(nums = [7,6,8], queries = [[0,0,2],[0,1,5],[2,2,5],[0,2,4]]),
        )

if __name__ == "__main__":
    unittest.main()

