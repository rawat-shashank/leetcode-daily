from re import split
import unittest
from typing import List


class PrefixTree:
    def __init__(self):
        self.children = {}
        self.end_of_folder = False

    def add(self, path):
        cur = self
        for f in path.split("/"):
            if f not in cur.children:
                cur.children[f] = PrefixTree()
            cur = cur.children[f]
        cur.end_of_folder = True

    def prefix_search(self, path):
        cur = self
        folders = path.split("/")
        for i in range(len(folders) - 1):
            cur = cur.children[folders[i]]
            if cur.end_of_folder:
                return True
        return False


class Solution:
    # def removeSubfolders(self, folder: List[str]) -> List[str]:
    #     """ hashmap with brute force"""
    #     folder_set = set(folder)
    #     res = []
    #     for f in folder:
    #         res.append(f)
    #         for i in range(len(f)):
    #             if f[i] == "/" and f[:i] in folder_set:
    #                 res.pop()
    #                 break
    #     return res
    #

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """prefix tree solution uses extra Tree for this"""
        prefix_tree = PrefixTree()

        for f in folder:
            prefix_tree.add(f)

        res = []

        print(prefix_tree.__str__)
        for f in folder:
            if not prefix_tree.prefix_search(f):
                res.append(f)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            ["/a", "/c/d", "/c/f"],
            self.sol.removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]),
        )

    def testcase2(self):
        self.assertEqual(
            ["/a"],
            self.sol.removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"]),
        )

    def testcase3(self):
        self.assertEqual(
            ["/a/b/c", "/a/b/ca", "/a/b/d"],
            self.sol.removeSubfolders(folder=["/a/b/c", "/a/b/ca", "/a/b/d"]),
        )


if __name__ == "__main__":
    unittest.main()
