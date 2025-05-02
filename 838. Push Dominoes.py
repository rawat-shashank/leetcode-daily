import unittest


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        force = [0] * N
        f = 0
        # calculate force left to right
        for i in range(N):
            if dominoes[i] == "R":
                f = N
            elif dominoes[i] == "L":
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] += f

        f = 0
        # calculate force right to left
        for i in range(N - 1, -1, -1):
            if dominoes[i] == "L":
                f = N
            elif dominoes[i] == "R":
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] -= f
        return "".join("." if f == 0 else "R" if f > 0 else "L" for f in force)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            "RR.L",
            self.sol.pushDominoes(dominoes="RR.L"),
        )

    def testcase2(self):
        self.assertEqual(
            "LL.RR.LLRRLL..",
            self.sol.pushDominoes(dominoes=".L.R...LR..L.."),
        )


if __name__ == "__main__":
    unittest.main()
