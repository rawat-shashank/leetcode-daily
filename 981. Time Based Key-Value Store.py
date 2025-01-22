import unittest


class TimeMap:

    def __init__(self):
        self.dp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dp:
            self.dp[key] = []
        self.dp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        arr = self.dp.get(key, [])
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res


class Testcases(unittest.TestCase):

    def testcase1(self):
        self.sol = TimeMap()
        self.sol.set(key="foo", value="bar", timestamp=1)
        self.assertEqual("bar", self.sol.get(key="foo", timestamp=1))
        self.assertEqual("bar", self.sol.get(key="foo", timestamp=3))

        self.sol.set(key="foo", value="bar2", timestamp=4)
        self.assertEqual("bar2", self.sol.get(key="foo", timestamp=4))
        self.assertEqual("bar2", self.sol.get(key="foo", timestamp=5))


if __name__ == "__main__":
    unittest.main()
