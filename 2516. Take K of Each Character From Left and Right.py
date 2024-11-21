import unittest


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        s_len = len(s)
        freq = [0] * 3
        for ch in s:
            freq[ord(ch) - ord("a")] += 1

        for count in freq:
            if count < k:
                return -1

        left = right = 0
        window = [0] * 3
        window_len = 0
        while right < s_len:
            window[ord(s[right]) - ord("a")] += 1
            while left <= right and (
                freq[0] - window[0] < k
                or freq[1] - window[1] < k
                or freq[2] - window[2] < k
            ):
                window[ord(s[left]) - ord("a")] -= 1
                left += 1
            window_len = max(window_len, right - left + 1)
            right += 1
        return s_len - window_len


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            8,
            self.sol.takeCharacters(s="aabaaaacaabc", k=2),
        )

    def testcase2(self):
        self.assertEqual(
            -1,
            self.sol.takeCharacters(s="a", k=1),
        )


if __name__ == "__main__":
    unittest.main()
