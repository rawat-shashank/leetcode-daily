import unittest

class Solution:

    # def minimumRecolors(self, blocks: str, k: int) -> int:
    #     left, right =0 ,0
    #     whites = 0
    #     res = float("inf")
    #     while right < len(blocks):
    #         if blocks[right] == 'W':
    #             whites += 1
    #         if right - left == k - 1:
    #             res = min(res, whites)
    #             if whites:
    #                 if blocks[left] == 'W':
    #                     whites -= 1
    #                 left += 1
    #         right += 1
    #     return res

    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        for ch in blocks[:k]:
            if ch == 'W':
                whites+=1
        res, left = whites, 0
        for i in range(k, len(blocks)):
            if blocks[left] == 'W':
                whites -= 1
            left+=1
            if blocks[i] == 'W':
                whites += 1
            res = min(res, whites)
        return res




class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            3,
            self.sol.minimumRecolors(blocks = "WBBWWBBWBW", k = 7),
        )

    def testcase2(self):
        self.assertEqual(
            0,
            self.sol.minimumRecolors(blocks = "WBWBBBW", k = 2),
        )

    def testcase3(self):
        self.assertEqual(
            3,
            self.sol.minimumRecolors(blocks = "BWWWBB", k = 6),
        )

if __name__ == "__main__":
    unittest.main()
