from typing import List
from heapq import heappop, heappush
import unittest


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        indexes = [i for i in range(len(times))]
        indexes.sort(key=lambda i: times[i][0])

        used_chairs = []
        available_chairs = [i for i in range(len(times))]

        for i in indexes:
            arrival, leave = times[i]
            while used_chairs and used_chairs[0][0] <= arrival:
                _, chair = heappop(used_chairs)
                heappush(available_chairs, chair)

            chair = heappop(available_chairs)
            heappush(used_chairs, (leave, chair))

            if i == targetFriend:
                return chair


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            1, self.sol.smallestChair(times=[[1, 4], [2, 3], [4, 6]], targetFriend=1)
        )

    def testcase2(self):
        self.assertEqual(
            2, self.sol.smallestChair(times=[[3, 10], [1, 5], [2, 6]], targetFriend=0)
        )


if __name__ == "__main__":
    unittest.main()
