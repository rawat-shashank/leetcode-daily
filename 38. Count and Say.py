import unittest
from collections import Counter


class Solution:
    def countAndSay(self, n: int) -> str:
        """burte force"""

        def dfs(n):
            if n == 1:
                return "1"

            tmp = dfs(n - 1)
            res = []
            count = 1
            if len(tmp) == 1:
                res.append(str(count))
                res.append(tmp)
            else:
                for i in range(1, len(tmp)):
                    if tmp[i - 1] == tmp[i]:
                        count += 1
                    if tmp[i - 1] != tmp[i]:
                        res.append(str(count))
                        res.append(tmp[i - 1])
                        count = 1
                res.append(str(count))
                res.append(tmp[-1])
            print(res)

            return "".join(res)

        return dfs(n)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertCountEqual("1211", self.sol.countAndSay(n=4))

    def testcase2(self):
        self.assertCountEqual("1", self.sol.countAndSay(n=1))

    def testcase3(self):
        self.assertCountEqual("111221", self.sol.countAndSay(n=5))


if __name__ == "__main__":
    unittest.main()
