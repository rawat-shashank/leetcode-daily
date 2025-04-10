import unittest


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        seen = set()
        for num in nums:
            if num < k:
                return -1
            elif num > k:
                seen.add(num)
        return len(seen)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.minOperations(nums = [5,2,5,4,5], k = 2),
        )

    def testcase2(self):
        self.assertEqual(
            -1,
            self.sol.minOperations(nums = [2,1,2], k = 2),
        )

    def testcase3(self):
        self.assertEqual(
            4,
            self.sol.minOperations(nums = [9,7,5,3], k = 1),
        )


if __name__ == "__main__":
    unittest.main()
