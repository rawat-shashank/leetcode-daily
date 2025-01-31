import unittest


class Node:
    def __init__(self, key: int, val: int) -> None:
        """custom doubly linked list, key is for hashmap"""
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        # using two node left for least used and right for recently used node
        self.left, self.right = Node(0, 0), Node(0, 0)
        # initialize the list with two nodes connected
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node: Node) -> None:
        """helper function to insert node before the rightmost node"""
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def remove(self, node: Node) -> None:
        """helper function to remove the current node"""
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        """if the key is in map, remove the node from the list
        insert it into rightmost position and return it's value
        else return -1"""
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        """if key is present, remove it from the list, add before the rightmost
        node, update the value in map"""
        if key in self.map:
            self.remove(self.map[key])
        self.map[key] = Node(key, value)
        self.insert(self.map[key])

        # make sure to check if it is inside capacity
        if len(self.map) > self.capacity:
            node = self.left.next
            self.remove(node)
            del self.map[node.key]


class TestLRUCache(unittest.TestCase):

    def testcase1(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        self.assertEqual(lru.get(1), 1)
        lru.put(3, 3)
        self.assertEqual(lru.get(2), -1)
        lru.put(4, 4)
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(3), 3)
        self.assertEqual(lru.get(4), 4)


if __name__ == "__main__":
    unittest.main()
