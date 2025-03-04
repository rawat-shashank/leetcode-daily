import unittest
from heapq import heapify, heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.nums, self.k = nums, k
        heapify(self.nums)
        while len(self.nums) > self.k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        while len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]

class Testcases(unittest.TestCase):

    def testcase1(self) -> None:
        commands = ["KthLargest", "add", "add", "add", "add", "add"]
        inputs = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
        expected_outputs = [None, 4, 5, 5, 8, 8]

        obj = None
        actual_outputs = []
        for i, command in enumerate(commands):
            if command == "KthLargest":
                obj = KthLargest(k=inputs[0][0], nums=inputs[0][1])
                actual_outputs.append(None)
            elif command == "add":
                actual_outputs.append(obj.add(inputs[i][0]))

        self.assertEqual(actual_outputs, expected_outputs)

    def testcase2(self) -> None:
        commands = ["KthLargest", "add", "add", "add", "add"]
        inputs = [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
        expected_outputs = [None, 7, 7, 7, 8]

        obj = None
        actual_outputs = []
        for i, command in enumerate(commands):
            if command == "KthLargest":
                obj = KthLargest(k=inputs[0][0], nums=inputs[0][1])
                actual_outputs.append(None)
            elif command == "add":
                actual_outputs.append(obj.add(inputs[i][0]))

        self.assertEqual(actual_outputs, expected_outputs)

if __name__ == "__main__":
    _ = unittest.main()
