
import unittest
from collections import Counter, deque
from heapq import heapify, heappop, heappush


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-count for count in freq.values()]
        heapify(maxHeap)
        
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                count = 1 + heappop(maxHeap)
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heappush(maxHeap, q.popleft()[0])
        return time
        


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            8,
            self.sol.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2),
        )

    def testcase2(self):
        self.assertEqual(
            6,
            self.sol.leastInterval(tasks = ["A","C","A","B","D","B"], n = 1),
        )

    def testcase3(self):
        self.assertEqual(
            10,
            self.sol.leastInterval(tasks = ["A","A","A", "B","B","B"], n = 3),
        )


if __name__ == "__main__":
    unittest.main()
