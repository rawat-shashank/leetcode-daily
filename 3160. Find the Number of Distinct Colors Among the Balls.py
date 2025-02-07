from typing import List
import unittest


class Solution:
    # def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
    #     """TLE - brute force"""
    #     balls = [0] * (limit + 1)
    #     colors = {}
    #     res = []
    #     for idx, color in queries:
    #         if balls[idx] == color and res:
    #             res.append(res[-1])
    #             continue
    #         if balls[idx]:
    #             colors[balls[idx]] -= 1
    #         if color not in colors:
    #             colors[color] = 1
    #         else:
    #             colors[color] += 1
    #         balls[idx] = color
    #         temp = 0
    #         for val in colors.values():
    #             temp += 1 if val > 0 else 0
    #         res.append(temp)
    #         print(res)
    #     return res

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = {}
        balls = {}
        res = []
        cnt = 0
        for ball, color in queries:
            if ball in balls:
                # removing prev_color so it's easier to count cuurent colors
                if colors[balls[ball]] == 1:
                    # a color is being removed
                    cnt -= 1
                    del colors[balls[ball]]
                else:
                    colors[balls[ball]] -= 1
            balls[ball] = color

            if color in colors:
                colors[color] += 1
            else:
                # a new color is intorduced
                cnt += 1
                colors[color] = 1
            res.append(cnt)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [1, 2, 2, 3],
            self.sol.queryResults(limit=4, queries=[[1, 4], [2, 5], [1, 3], [3, 4]]),
        )

    def testcase2(self):
        self.assertEqual(
            [1, 2, 2, 3, 4],
            self.sol.queryResults(
                limit=4, queries=[[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
            ),
        )

    def testcase3(self):
        self.assertEqual(
            [1, 1, 1, 1, 2],
            self.sol.queryResults(
                limit=1, queries=[[0, 1], [0, 4], [0, 4], [0, 1], [1, 2]]
            ),
        )


if __name__ == "__main__":
    unittest.main()
