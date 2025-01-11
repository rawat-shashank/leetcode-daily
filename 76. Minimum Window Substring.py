import unittest


class Solution:
    # def minWindow(self, s: str, t: str) -> str:
    #     """correct but TLE"""
    #     dp1 = {}
    #     for ch in t:
    #         dp1[ch] = dp1.get(ch, 0) + 1
    #
    #     def isSubString(word):
    #         dp2 = {}
    #         for x in word:
    #             dp2[x] = dp2.get(x, 0) + 1
    #
    #         for x in dp1.keys():
    #             if dp2.get(x) and dp2[x] >= dp1[x]:
    #                 continue
    #             else:
    #                 return False
    #         return True
    #
    #     # if len(t) > len(s):
    #     #     return ""
    #     start, end = 0, 0
    #     minStart, minEnd = 0, float("inf")
    #     while end < len(s):
    #         if isSubString(s[start : end + 1]):
    #             # print(s[start : end + 1])
    #             if end - start < minEnd - minStart:
    #                 minStart = start
    #                 minEnd = end
    #             else:
    #                 start += 1
    #         else:
    #             end += 1
    #
    #     return "" if minEnd == float("inf") else s[minStart : minEnd + 1]

    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "":
            return ""

        countT, window = {}, {}
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        left = 0
        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            # check if current char is in countT and
            # there count is now equal
            if ch in countT and window[ch] == countT[ch]:
                have += 1

            while have == need:
                # update result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                # adjust left towards right to find minimum window required
                window[s[left]] -= 1
                # check if we can remove leftmost characters safely
                # without breaking valid window
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return "" if resLen == float("inf") else s[left : right + 1]


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            "BANC",
            self.sol.minWindow(s="ADOBECODEBANC", t="ABC"),
        )

    def testcase2(self):
        self.assertEqual(
            "a",
            self.sol.minWindow(s="a", t="a"),
        )

    def testcase3(self):
        self.assertEqual(
            "",
            self.sol.minWindow(s="a", t="aa"),
        )

    def testcase4(self):
        self.assertEqual(
            "",
            self.sol.minWindow(s="a", t="b"),
        )


if __name__ == "__main__":
    unittest.main()
