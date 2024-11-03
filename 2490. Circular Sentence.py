import unittest


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # """o(n) with o(n) space"""
        # words = sentence.split(" ")
        # for i in range(len(words)):
        #     if words[i][0] != words[i - 1][-1]:
        #         return False
        # return True

        """O(n) with O(1) space, not extra space required"""
        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i - 1] != sentence[i + 1]:
                return False
        return sentence[0] == sentence[-1]


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.isCircularSentence(sentence="leetcode exercises sound delightful"),
        )

    def testcase2(self):
        self.assertTrue(
            self.sol.isCircularSentence(sentence="eetcode"),
        )

    def testcase3(self):
        self.assertFalse(
            self.sol.isCircularSentence(sentence="Leetcode is cool"),
        )

    def testcase4(self):
        self.assertFalse(
            self.sol.isCircularSentence(sentence="MuFoevIXCZzrpXeRmTssj lYSW U jM"),
        )


if __name__ == "__main__":
    unittest.main()
