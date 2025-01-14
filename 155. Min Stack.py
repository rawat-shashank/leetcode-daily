import unittest


class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val is None or min_val > val:
            min_val = val
        self.data.append([val, min_val])

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0] if self.data else None

    def getMin(self) -> int:
        return self.data[-1][1] if self.data else None


class Testcases(unittest.TestCase):

    def testcase1(self):
        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)

        self.assertEqual(-3, obj.getMin())
        obj.pop()
        self.assertEqual(0, obj.top())
        self.assertEqual(-2, obj.getMin())


if __name__ == "__main__":
    unittest.main()
