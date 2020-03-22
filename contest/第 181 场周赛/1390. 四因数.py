# -*- coding:utf-8 -*-

"""
给你一个整数数组 nums，请你返回该数组中恰有四个因数的这些整数的各因数之和。
如果数组中不存在满足题意的整数，则返回 0 。

示例：
输入：nums = [21,4,7]
输出：32
解释：
21 有 4 个因数：1, 3, 7, 21
4 有 3 个因数：1, 2, 4
7 有 2 个因数：1, 7
答案仅为 21 的所有因数的和。

提示：

1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def get_divisor_sum(self, num):
        """
        获取四因数的数字的因数之和
        :param num:
        :return:
        """
        res = 1 + num
        t = 2
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                if i * i == num:
                    t += 1
                    res += i
                else:
                    t += 2
                    res += i + num // i
                if t > 4:
                    return 0
        return res if t == 4 else 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res += self.get_divisor_sum(num)
        return res
