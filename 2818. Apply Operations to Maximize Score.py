import unittest
from heapq import heapify, heappop
from math import sqrt


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:

        N = len(nums)
        MOD = 10**9 + 7
        res = 1

        # get prime score(distinct prime factors)
        prime_scores = []
        for n in nums:
            score = 0
            for factor in range(2, int(sqrt(n)) + 1):
                if n % factor == 0:
                    score += 1
                    while n % factor == 0:
                        n = n // factor
            if n >= 2:
                score += 1
            prime_scores.append(score)

        # get left and right bound values using strictly decreasing monotonic stack
        left_bound = [-1] * N
        right_bound = [N] * N
        stack = []
        for idx, score in enumerate(prime_scores):
            # making sure stack only have decreasing values
            while stack and prime_scores[stack[-1]] < score:
                index = stack.pop()
                right_bound[index] = idx
            if stack:
                left_bound[idx] = stack[-1]
            stack.append(idx)

        # use heap to maximise return values
        heap = [(-n, idx) for idx, n in enumerate(nums)]
        heapify(heap)
        while k > 0:
            n, idx = heappop(heap)
            n = -n
            score = prime_scores[idx]
            left_cnt = idx - left_bound[idx]
            right_cnt = right_bound[idx] - idx

            count = left_cnt * right_cnt
            operations = min(count, k)
            res = (res * pow(n, operations, MOD)) % MOD
            k -= operations

        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            81,
            self.sol.maximumScore(nums=[8, 3, 9, 3, 8], k=2),
        )

    def testcase2(self):
        self.assertEqual(
            4788,
            self.sol.maximumScore(nums=[19, 12, 14, 6, 10, 18], k=3),
        )


if __name__ == "__main__":
    unittest.main()
