import unittest
from typing import List
from heapq import heapify, heappop


class Solution:

    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    #     """using stacks"""
    #     stack = []
    #     res = [[pos, sp] for pos, sp in zip(position, speed)]
    #     for pos, sp in sorted(res)[::-1]:
    #         print(pos, sp)
    #         stack.append((target - pos) / sp)
    #         if len(stack) > 1 and stack[-1] <= stack[-2]:
    #             stack.pop()
    #     return len(stack)
    #
    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    #     """using stacks with min heap"""
    #     stack = []
    #     res = [[-pos, sp] for pos, sp in zip(position, speed)]
    #     heapify(res)
    #     while res:
    #         pos, sp = heappop(res)
    #         stack.append((target + pos) / sp)
    #         if len(stack) > 1 and stack[-1] <= stack[-2]:
    #             stack.pop()
    #     return len(stack)

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        min_acc = float("-inf")
        res = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        for pos, sp in res:
            acc = (target - pos) / sp
            if acc > min_acc:
                fleet += 1
                min_acc = acc
        return fleet


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            3,
            self.sol.carFleet(
                target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]
            ),
        )

    def testcase2(self):
        self.assertEqual(
            1,
            self.sol.carFleet(target=10, position=[3], speed=[3]),
        )

    def testcase3(self):
        self.assertEqual(
            1,
            self.sol.carFleet(target=100, position=[0, 2, 4], speed=[4, 2, 1]),
        )


if __name__ == "__main__":
    unittest.main()
