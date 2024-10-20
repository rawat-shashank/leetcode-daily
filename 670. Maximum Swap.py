import unittest


class Solution:
    def maximumSwaps(self, num: int) -> int:
        """Brute Force"""
        nums_str = str(num)
        nums_len = len(nums_str)
        max_num = num
        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                nums_list = list(nums_str)
                nums_list[i], nums_list[j] = (nums_list[j], nums_list[i])
                max_num = max(max_num, int("".join(nums_list)))
        return max_num

    def maximumSwaps1(self, num: int) -> int:
        """Greedy 2 Pass"""
        num_str = list(str(num))
        nums_len = len(num_str)
        max_right_index = [0] * nums_len

        max_right_index[nums_len - 1] = nums_len - 1
        for i in range(nums_len - 2, -1, -1):
            max_right_index[i] = (
                i
                if num_str[i] > num_str[max_right_index[i + 1]]
                else max_right_index[i + 1]
            )

        for i in range(nums_len):
            if num_str[i] < num_str[max_right_index[i]]:
                num_str[i], num_str[max_right_index[i]] = (
                    num_str[max_right_index[i]],
                    num_str[i],
                )
                return int("".join(num_str))
        return num


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            7236,
            self.sol.maximumSwaps1(num=2736),
        )

    def testcase2(self):
        self.assertEqual(9973, self.sol.maximumSwaps1(num=9973))

    def testcase3(self):
        self.assertEqual(98863, self.sol.maximumSwaps1(num=98368))


if __name__ == "__main__":
    unittest.main()
