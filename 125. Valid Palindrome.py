import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            right -= 1
            left += 1
        return True


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.isPalindrome(s="A man, a plan, a canal: Panama"),
        )

    def testcase2(self):
        self.assertFalse(
            self.sol.isPalindrome(s="race a car"),
        )

    def testcase3(self):
        self.assertTrue(
            self.sol.isPalindrome(s=" "),
        )

    def testcase4(self):
        self.assertTrue(
            self.sol.isPalindrome(s=".,"),
        )

    def testcase5(self):
        self.assertFalse(
            self.sol.isPalindrome(s="0P"),
        )


if __name__ == "__main__":
    unittest.main()
