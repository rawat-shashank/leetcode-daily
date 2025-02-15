import unittest


class Solution:
    def punishmentNumber(self, n: int) -> int:
        """brute force"""

        def can_partition(num, target):
            # Invalid partition found
            if target < 0 or num < target:
                return False

            # Valid partition found
            if num == target:
                return True

            # Recursively check all partitions for a valid partition
            return (
                can_partition(num // 10, target - num % 10)
                or can_partition(num // 100, target - num % 100)
                or can_partition(num // 1000, target - num % 1000)
            )

        res = 0
        for i in range(1, n + 1):
            if can_partition(i * i, i):
                res += i * i
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            182,
            self.sol.punishmentNumber(n=10),
        )

    def testcase2(self):
        self.assertEqual(
            1478,
            self.sol.punishmentNumber(n=37),
        )


if __name__ == "__main__":
    unittest.main()
