import unittest


class Solution:
    # def getHappyString(self, n: int, k: int) -> str:
    #     """backtrack easy - accepted - not fast"""
    #     res = []
    #
    #     def backtrack(current_string):
    #         if len(current_string) == n:
    #             res.append(current_string)
    #             return
    #
    #         for ch in ["a", "b", "c"]:
    #             if len(current_string) > 0 and current_string[-1] == ch:
    #                 continue
    #             backtrack(current_string + ch)
    #
    #     backtrack("")
    #     return "" if k > len(res) else res[k - 1]

    def getHappyString(self, n: int, k: int) -> str:
        """math solution - O(n)"""

        # maximum no of string that can be
        total_happy = 3 * (2 ** (n - 1))
        res = []
        left, right = 1, total_happy
        choices = "abc"

        for i in range(n):
            curr = left
            partian_size = (right - left + 1) // len(choices)

            for ch in choices:
                if k in range(curr, curr + partian_size):
                    res.append(ch)
                    left = curr
                    right = curr + partian_size - 1
                    choices = "abc".replace(ch, "")
                    break
                curr += partian_size

        return "".join(res)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual("c", self.sol.getHappyString(n=1, k=3))

    def testcase2(self):
        self.assertEqual("", self.sol.getHappyString(n=1, k=4))

    def testcase3(self):
        self.assertEqual("cab", self.sol.getHappyString(n=3, k=9))


if __name__ == "__main__":
    unittest.main()
