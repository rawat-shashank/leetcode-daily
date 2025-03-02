import unittest

class Solution:

    # def applyOperations(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    #     """soltution with min heap, accepted but not fast"""
    #     res: list[list[int]] = []
    #     heapify(nums1)
    #     heapify(nums2)
    #     while nums1 or nums2:
    #         pos1, val1 = heappop(nums1) if nums1 else [0,0]
    #         pos2, val2 = heappop(nums2) if nums2 else [0,0]
    #         if pos1 == pos2:
    #             res.append([pos1, val1+val2])
    #         elif not pos1:
    #             res.append([pos2, val2])
    #         elif not pos2:
    #             res.append([pos1, val1])
    #         elif pos1 < pos2:
    #             res.append([pos1, val1])
    #             heappush(nums2, [pos2, val2])
    #         else:
    #             res.append([pos2, val2])
    #             heappush(nums1, [pos1, val1])
    #     return res

    def applyOperations(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        """using hashmap"""
        dp: dict[int,int] = {}
        for pos, val in nums1:
            dp[pos] = val
        for pos, val in nums2:
            if pos in dp:
                dp[pos] += val
            else:
                dp[pos] = val
        res: list[list[int]] = []
        for pos in sorted(dp.keys()):
            res.append([pos, dp[pos]])
        return res


class Testcases(unittest.TestCase):

    def testcase1(self) -> None:
        self.assertEqual(
            first=[[1,6],[2,3],[3,2],[4,6]],
            second=Solution().applyOperations(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]),
        )

    def testcase2(self) -> None:
        self.assertEqual(
            first=[[1,3],[2,4],[3,6],[4,3],[5,5]],
            second=Solution().applyOperations(nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]),
        )


if __name__ == "__main__":
    unittest.main()
