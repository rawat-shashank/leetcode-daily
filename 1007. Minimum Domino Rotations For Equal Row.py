import unittest


class Solution:

    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)

        def check(target):
            rotations_top = 0
            rotations_bottom = 0
            possible_top = True
            possible_bottom = True
            for i in range(n):
                # Check for making tops all target
                if tops[i] != target and bottoms[i] != target:
                    possible_top = False
                elif tops[i] != target:
                    rotations_top += 1

                # Check for making bottoms all target
                if bottoms[i] != target and tops[i] != target:
                    possible_bottom = False
                elif bottoms[i] != target:
                    rotations_bottom += 1

            top_rotations = rotations_top if possible_top else float("inf")
            bottom_rotations = rotations_bottom if possible_bottom else float("inf")
            return min(top_rotations, bottom_rotations)

        ans = float("inf")
        ans = min(ans, check(tops[0]))
        ans = min(ans, check(bottoms[0]))
        return ans if ans != float("inf") else -1


class Testcases(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.minDominoRotations(
                tops=[2, 1, 2, 4, 2, 2], bottoms=[5, 2, 6, 2, 3, 2]
            ),
        )

    def testcase2(self):
        self.assertEqual(
            -1,
            self.sol.minDominoRotations(tops=[3, 5, 1, 2, 3], bottoms=[3, 6, 3, 3, 4]),
        )


if __name__ == "__main__":
    unittest.main()
