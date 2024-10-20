import unittest


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        seqs = "0"

        for _ in range(1, n):
            if k <= len(seqs):
                break
            seqs += "1"

            inverted = "".join("1" if bit == "0" else "0" for bit in seqs[:-1])
            seqs += inverted[::-1]

        return seqs[k - 1]


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            "0",
            self.sol.findKthBit(n=3, k=1),
        )

    def testcase2(self):
        self.assertEqual("1", self.sol.findKthBit(n=4, k=11))


if __name__ == "__main__":
    unittest.main()
