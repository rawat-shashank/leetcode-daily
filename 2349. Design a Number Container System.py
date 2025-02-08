import unittest
from heapq import heappop, heappush
from collections import defaultdict


class NumberContainers:

    def __init__(self):
        # from index to number hasmap
        self.idx_num_map = {}
        # from number to index heap for min idx fast retierval
        self.number_to_idx_map = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        # add or update the number at given index
        self.idx_num_map[index] = number
        heappush(self.number_to_idx_map[number], index)

    def find(self, number: int) -> int:
        if not self.number_to_idx_map[number]:
            return -1

        while self.number_to_idx_map[number]:
            idx = self.number_to_idx_map[number][0]
            if self.idx_num_map.get(idx) == number:
                return idx
            # remove stale data
            heappop(self.number_to_idx_map[number])
        return -1


class TestNumberContainersClass(unittest.TestCase):

    def test_case1(self):
        number_containers = NumberContainers()
        self.assertEqual(number_containers.find(10), -1)
        number_containers.change(2, 10)
        number_containers.change(1, 10)
        number_containers.change(3, 10)
        number_containers.change(5, 10)
        self.assertEqual(number_containers.find(10), 1)
        number_containers.change(1, 20)
        self.assertEqual(number_containers.find(10), 2)


if __name__ == "__main__":
    unittest.main()
