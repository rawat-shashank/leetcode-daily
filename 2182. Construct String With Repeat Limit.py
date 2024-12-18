import unittest
from heapq import heappush, heappop


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        dp = {}
        for ch in s:
            dp[ch] = dp.get(ch, 0) + 1
        res = []
        for ch in dp.keys():
            heappush(res, (-ord(ch), dp[ch]))
        ans = []
        while res:
            ch, freq = heappop(res)
            if freq > repeatLimit:
                ans.append(chr(-ch) * repeatLimit)
                if res:
                    ch1, freq1 = heappop(res)
                    ans.append(chr(-ch1))
                    freq1 -= 1
                    if freq1 > 0:
                        heappush(res, (ch1, freq1))
                    heappush(res, (ch, freq - repeatLimit))
                else:
                    break
            else:
                ans.append(chr(-ch) * freq)
        return "".join(ans)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            "zzcccac", self.sol.repeatLimitedString(s="cczazcc", repeatLimit=3)
        )

    def testcase2(self):
        self.assertEqual(
            "bbabaa", self.sol.repeatLimitedString(s="aababab", repeatLimit=2)
        )

    def testcase3(self):
        self.assertEqual(
            "zyxyxwxwvwvuvuvututstrtrtqpqpqponononmlmkmkjigifiededededcbaba",
            self.sol.repeatLimitedString(
                s="xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt",
                repeatLimit=1,
            ),
        )


if __name__ == "__main__":
    unittest.main()
