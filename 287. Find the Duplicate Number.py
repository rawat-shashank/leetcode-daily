import unittest
from typing import List


class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    #     """using input array as hashmap - similar to linked list using
    #     value as next pointer which will be val - 1 for this problem
    #     setting in negative to mark it as visited instead of postive
    #     val we are using for iteration
    #     """
    #     for num in nums:
    #         idx = abs(num) - 1
    #         if nums[idx] < 0:
    #             return abs(num)
    #         else:
    #             nums[idx] *= -1
    #     return -1

    def findDuplicate(self, nums: List[int]) -> int:
        """slow fast pointer -> it will work for this problem as it say only
        one number will be repeated, so there will be one cycle only
        similar to slow ans fast traversal of linked list
        """
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.findDuplicate(nums=[1, 3, 4, 2, 2]),
        )

    def testcase2(self):
        self.assertEqual(
            3,
            self.sol.findDuplicate(nums=[3, 1, 3, 4, 2]),
        )

    def testcase3(self):
        self.assertEqual(
            3,
            self.sol.findDuplicate(nums=[3, 3, 3, 3, 3]),
        )


if __name__ == "__main__":
    unittest.main()
