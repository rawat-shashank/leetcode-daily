import unittest


class Solution:
    # def countDays(self, days:int, meetings: list[list[int]]) -> str:
    #     meetings.sort()
    #     prev_end = 0
    #     for start, end in meetings:
    #         start = max(start, prev_end + 1)
    #         length = end - start + 1
    #         days -= max(length, 0 )
    #         prev_end = max(prev_end, end)
    #     return days

    def countDays(self, days:int, meetings: list[list[int]]) -> str:
        # using line sweep

class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]),
        )

    def testcase2(self):
        self.assertEqual(
            1,
            self.sol.countDays(days = 5, meetings = [[2,4],[1,3]]),
        )

    def testcase3(self):
        self.assertEqual(
            0,
            self.sol.countDays(days = 6, meetings = [[1,6]])
        )

if __name__ == "__main__":
    unittest.main()
