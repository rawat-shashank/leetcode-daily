from heapq import heappop, heappush
import unittest


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, maxHeap = "", []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heappop(maxHeap)
                res += char2
                count2 += 1  # since the counts are in negative
                if count2:
                    heappush(maxHeap, (count2, char2))

            else:
                res += char
                count += 1  # since the counts are in negative

            if count:
                heappush(maxHeap, (count, char))

        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            "ccaccbcc",
            self.sol.longestDiverseString(a=1, b=1, c=7),
        )

    def testcase2(self):
        self.assertEqual("aabaa", self.sol.longestDiverseString(a=7, b=1, c=0))


if __name__ == "__main__":
    unittest.main()
