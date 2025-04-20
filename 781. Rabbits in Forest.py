import unittest


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        answers.sort()
        res = 0
        count = 0
        for i in range(len(answers)):
            # if there is only one rabbit of this color
            if answers[i] == 0:
                res += 1
            # update res if no new color is comming
            elif i == 0 or answers[i] != answers[i - 1] or count == 0:
                res += answers[i] + 1
                count = answers[i]
            # remove if same color is repeating until we have all rabits
            else:
                count -= 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            5,
            self.sol.numRabbits(answers=[1, 1, 2]),
        )

    def testcase2(self):
        self.assertEqual(11, self.sol.numRabbits(answers=[10, 10, 10]))


if __name__ == "__main__":
    unittest.main()
