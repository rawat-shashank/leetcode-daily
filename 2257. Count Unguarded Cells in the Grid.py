import unittest
from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        # 0 - unguarded, walls = 2, guards=1 and guarded = 3
        ans = [[0] * n for i in range(m)]
        for wall in walls:
            row, col = wall
            ans[row][col] = 2
        for guard in guards:
            row, col = guard
            ans[row][col] = 1

        def check_guard(i, j, guard):
            if ans[i][j] == 1:
                return True
            if ans[i][j] == 2:
                return False
            if guard and not ans[i][j]:
                ans[i][j] = 3
            return guard

        """check two pass horizontally, one in each direction"""
        for row in range(m):
            guard = False
            for col in range(n):
                guard = check_guard(row, col, guard)
            guard = False
            for col in range(n - 1, -1, -1):
                guard = check_guard(row, col, guard)
        """check two pass vertically, one in each direction"""
        for col in range(n):
            guard = False
            for row in range(m):
                guard = check_guard(row, col, guard)
            guard = False
            for row in range(m - 1, -1, -1):
                guard = check_guard(row, col, guard)

        count = 0
        for row in ans:
            for val in row:
                if not val:
                    count += 1
        return count


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            7,
            self.sol.countUnguarded(
                m=4,
                n=6,
                guards=[[0, 0], [1, 1], [2, 3]],
                walls=[[0, 1], [2, 2], [1, 4]],
            ),
        )

    def testcase2(self):
        self.assertEqual(
            4,
            self.sol.countUnguarded(
                m=3, n=3, guards=[[1, 1]], walls=[[0, 1], [1, 0], [2, 1], [1, 2]]
            ),
        )


if __name__ == "__main__":
    unittest.main()
