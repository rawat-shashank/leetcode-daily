import unittest
from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """backtracking"""

        # one 1 + two of each number
        res = [0] * (2 * n - 1)
        usedNums = set()

        def backTracking(i):
            if i == len(res):
                return True

            for num in reversed(range(1, n + 1)):
                # validation if number already used
                if num in usedNums:
                    continue

                # check if num is not one, it's second value is not
                # out of range or it was prepopulated
                if num > 1 and (i + num >= len(res) or res[i + num]):
                    continue

                # try the current number for current position
                usedNums.add(num)
                res[i] = num
                if num > 1:
                    res[i + num] = num

                # skip prepopulated numbers in res
                j = i + 1
                while j < len(res) and res[j]:
                    j += 1

                # recursivily check if next num in next position valid or nor
                if backTracking(j):
                    return True

                # if next item wasn't valid, backtrack
                usedNums.remove(num)
                res[i] = 0
                if num > 1:
                    res[i + num] = 0
            return False

        backTracking(0)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [3, 1, 2, 3, 2],
            self.sol.constructDistancedSequence(n=3),
        )

    def testcase2(self):
        self.assertEqual(
            [5, 3, 1, 4, 3, 5, 2, 4, 2],
            self.sol.constructDistancedSequence(n=5),
        )


if __name__ == "__main__":
    unittest.main()
