import unittest
from collections import defaultdict


class Solution:
    # def countPairs(self, nums: list[int], k: int) -> int:
    #     res = 0
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] == nums[j] and (i * j) % k == 0:
    #                 res += 1
    #     return res

    def countPairs(self, nums: list[int], k: int) -> int:
        dict = defaultdict(list)
        res = 0
        for i in range(len(nums)):
            for j in dict[nums[i]]:
                if (i * j) % k == 0:
                    res += 1
            dict[nums[i]].append(i)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(4, self.sol.countPairs(nums=[3, 1, 2, 2, 2, 1, 3], k=2))

    def testcase2(self):
        self.assertEqual(0, self.sol.countPairs(nums=[1, 2, 3, 4], k=1))


if __name__ == "__main__":
    unittest.main()
