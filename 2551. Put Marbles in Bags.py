import unittest

class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        if len(weights) == k:
            return 0
        splits = []
        for i in range(len(weights) - 1):
            splits.append(weights[i] + weights[i+1])

        splits.sort()
        max_score = sum(splits[-(k-1):])
        min_score = sum(splits[:k-1])
        return max_score - min_score


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            4,
            self.sol.putMarbles(weights = [1,3,5,1], k = 2),
        )

    def testcase2(self):
        self.assertEqual(0, self.sol.putMarbles(weights = [1, 3], k = 2))


if __name__ == "__main__":
    unittest.main()
