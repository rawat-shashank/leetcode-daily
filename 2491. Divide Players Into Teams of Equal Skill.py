import unittest
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)

        if (2 * total) % len(skill):
            return -1

        skill.sort()
        target = (2 * sum(skill)) // len(skill)
        left, rright, res = 0, len(skill) - 1, 0
        while left < rright:
            if skill[left] + skill[rright] == target:
                res += skill[left] * skill[rright]
                left += 1
                rright -= 1
            else:
                return -1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            22,
            self.sol.dividePlayers(skill=[3, 2, 5, 1, 3, 4]),
        )

    def testcase2(self):
        self.assertEqual(
            12,
            self.sol.dividePlayers(skill=[3, 4]),
        )

    def testcase3(self):
        self.assertEqual(
            -1,
            self.sol.dividePlayers(skill=[1, 1, 2, 3]),
        )


if __name__ == "__main__":
    unittest.main()
