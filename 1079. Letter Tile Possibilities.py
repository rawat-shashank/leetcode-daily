import unittest
from collections import Counter


class Solution:
    # def numTilePossibilities(self, tiles: str) -> int:
    #     """recursive backtrack on all char"""
    #     res = set()
    #     used = [False] * len(tiles)
    #
    #     def backtrack(current):
    #         res.add(current)
    #         for pos, ch in enumerate(tiles):
    #             if not used[pos]:
    #                 used[pos] = True
    #                 backtrack(current + ch)
    #                 used[pos] = False
    #
    #     backtrack("")
    #     return len(res) - 1

    def numTilePossibilities(self, tiles: str) -> int:
        """recursive backtrack on char counts instead of making strings"""
        counts = Counter(tiles)

        def backtrack():
            res = 0

            for count in counts:
                # this will handle the base case where there
                # is no more char left in tiles
                if counts[count] > 0:
                    counts[count] -= 1
                    res += 1
                    res += backtrack()
                    counts[count] += 1
            return res

        return backtrack()


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            8,
            self.sol.numTilePossibilities(tiles="AAB"),
        )

    def testcase2(self):
        self.assertEqual(
            188,
            self.sol.numTilePossibilities(tiles="AAABBC"),
        )

    def testcase3(self):
        self.assertEqual(
            1,
            self.sol.numTilePossibilities(tiles="V"),
        )


if __name__ == "__main__":
    unittest.main()
