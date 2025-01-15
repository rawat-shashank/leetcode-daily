import unittest


class Solution:

    def minimizeXor(self, num1: int, num2: int) -> int:

        given_bits_count = bin(num1).count("1")
        target_bits_count = bin(num2).count("1")

        x = num1
        i = 0
        while given_bits_count != target_bits_count:
            if given_bits_count > target_bits_count and x & (1 << i):
                given_bits_count -= 1
                x = x ^ (1 << i)
            if given_bits_count < target_bits_count and x & (1 << i) == 0:
                given_bits_count += 1
                x = x | (1 << i)
            i += 1
        return x


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(3, self.sol.minimizeXor(num1=3, num2=5))

    def testcase2(self):
        self.assertEqual(3, self.sol.minimizeXor(num1=1, num2=12))


if __name__ == "__main__":
    unittest.main()
