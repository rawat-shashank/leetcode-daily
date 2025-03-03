
import unittest

class Solution:

    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        before: list[int] = []
        after: list[int] = []
        pivotCount: int = 0
        for num in nums:
            if num < pivot:
                before.append(num)
            elif num > pivot:
                after.append(num)
            else:
                pivotCount += 1
        while pivotCount:
            before.append(pivot)
            pivotCount -= 1
        before.extend(after)
        print(before)
        return before


class Testcases(unittest.TestCase):

    def testcase1(self) -> None:
        self.assertEqual(
            first=[9,5,3,10,10,12,14],
            second=Solution().pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10),
        )

    def testcase2(self) -> None:
        self.assertEqual(
            first=[-3,2,4,3],
            second=Solution().pivotArray(nums = [-3,4,3,2], pivot = 2),
        )


if __name__ == "__main__":
    unittest.main()
