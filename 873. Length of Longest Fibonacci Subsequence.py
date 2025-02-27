import unittest

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        used: set[int] = set(arr)
        res = 0
        for i in range(len(arr) - 1):
            for j in range(i+ 1, len(arr)):
                prev, curr = arr[i], arr[j]
                nxt = prev + curr
                length = 2
                while nxt in used:
                    length += 1
                    prev, curr = curr, nxt
                    nxt = prev + curr
                    res = max(res, length)
        return res


class Testcases(unittest.TestCase):

    def testcase1(self) -> None:
        self.assertEqual(first=5, second=Solution().lenLongestFibSubseq(arr = [1,2,3,4,5,6,7,8]))

    def testcase2(self) -> None:
        self.assertEqual(first=3, second=Solution().lenLongestFibSubseq(arr = [1,3,7,11,12,14,18]))



if __name__ == "__main__":
    _ = unittest.main()
