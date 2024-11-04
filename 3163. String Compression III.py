import unittest


class Solution:
    def compressedString(self, word: str) -> str:
        left, right = 0, 1
        res = []
        count = 1
        while right < len(word):
            if count == 9 or word[left] != word[right]:
                res.append(f"{count}{word[left]}")
                count = 1
                left = right

            else:
                count += 1

            right += 1
        if left != right:
            res.append(f"{count}{word[left]}")
        return "".join(res)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            "1a1b1c1d1e",
            self.sol.compressedString(word="abcde"),
        )

    def testcase2(self):
        self.assertEqual(
            "9a5a2b",
            self.sol.compressedString(word="aaaaaaaaaaaaaabb"),
        )


if __name__ == "__main__":
    unittest.main()
