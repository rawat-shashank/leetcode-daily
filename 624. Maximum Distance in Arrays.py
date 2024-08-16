# 455. Assign Cookies
import unittest
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0
        for arr in arrays[1::]:
            max_distance = max(max_distance, arr[-1] - smallest, biggest - arr[0])
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])
        return max_distance


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(4, self.sol.maxDistance(arrays=[[1, 2, 3], [4, 5], [1, 2, 3]]))

    def testcase2(self):
        self.assertEqual(0, self.sol.maxDistance(arrays=[[1], [1]]))

    def testcase3(self):
        self.assertEqual(4, self.sol.maxDistance(arrays=[[1,4],[0,5]]))
        


if __name__ == "__main__":
    unittest.main()
