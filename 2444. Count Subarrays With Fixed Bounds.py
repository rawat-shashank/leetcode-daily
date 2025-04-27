import unittest


class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        res = 0
        lastMinKIndex = -1
        lastMaxKIndex = -1
        lastInvalidIndex = -1
        for i in range(len(nums)):
            if nums[i] == minK:
                lastMinKIndex = i
            if nums[i] == maxK:
                lastMaxKIndex = i
            if nums[i] < minK or nums[i] > maxK:
                lastInvalidIndex = i
            res += max(0, min(lastMinKIndex, lastMaxKIndex) - lastInvalidIndex)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2, self.sol.countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5)
        )

    def testcase2(self):
        self.assertEqual(10, self.sol.countSubarrays(nums=[1, 1, 1, 1], minK=1, maxK=1))


if __name__ == "__main__":
    unittest.main()
