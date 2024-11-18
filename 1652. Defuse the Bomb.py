from typing import List
import unittest


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """using sliding window (mod from array len)"""
        code_len = len(code)
        if k == 0:
            return [0] * code_len

        start, end, window_sum = 1, k, 0
        if k < 0:
            start, end = code_len - abs(k), code_len - 1

        for i in range(start, end + 1):
            window_sum += code[i]

        res = [0] * code_len
        for i in range(code_len):
            res[i] = window_sum
            window_sum -= code[start % code_len]
            start += 1
            window_sum += code[(end + 1) % code_len]
            end += 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [12, 10, 16, 13],
            self.sol.decrypt(code=[5, 7, 1, 4], k=3),
        )

    def testcase2(self):
        self.assertEqual(
            [0, 0, 0, 0],
            self.sol.decrypt(code=[1, 2, 3, 4], k=0),
        )

    def testcase3(self):
        self.assertEqual(
            [12, 5, 6, 13],
            self.sol.decrypt(code=[2, 4, 9, 3], k=-2),
        )


if __name__ == "__main__":
    unittest.main()
