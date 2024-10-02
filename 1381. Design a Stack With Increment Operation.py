import unittest
from typing import List


class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.data = []

    def push(self, x: int) -> None:
        if len(self.data) < self.maxSize:
            self.data.append(x)

    def pop(self) -> int:
        return -1 if len(self.data) == 0 else self.data.pop()

    def increment(self, k: int, val: int) -> None:
        self.data = [x + val if idx < k else x for idx, x in enumerate(self.data)]

class TestCustomStack(unittest.TestCase):
    """
    Actual Input
    ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
    [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
    """
    def setUp(self):
        self.stack = CustomStack(3)  # Replace 3 with the desired capacity
        self.assertEqual(self.stack.maxSize, 3)
    
    def test_push_and_pops(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.increment(5, 100)
        self.stack.increment(2, 100)
        self.assertEqual(self.stack.pop(), 103)
        self.assertEqual(self.stack.pop(), 202)
        self.assertEqual(self.stack.pop(), 201)
        self.assertEqual(self.stack.pop(), -1)


if __name__ == "__main__":
    unittest.main()
