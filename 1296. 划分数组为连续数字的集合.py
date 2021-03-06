# -*- coding:utf-8 -*-

"""
给你一个整数数组 nums 和一个正整数 k，请你判断是否可以把这个数组划分成一些由 k 个连续数字组成的集合。
如果可以，请返回 True；否则，返回 False。

 

示例 1：

输入：nums = [1,2,3,3,4,4,5,6], k = 4
输出：true
解释：数组可以分成 [1,2,3,4] 和 [3,4,5,6]。
示例 2：

输入：nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
输出：true
解释：数组可以分成 [1,2,3] , [2,3,4] , [3,4,5] 和 [9,10,11]。
示例 3：

输入：nums = [3,3,2,2,1,1], k = 3
输出：true
示例 4：

输入：nums = [1,2,3,4], k = 3
输出：false
解释：数组不能分成几个大小为 3 的子数组。
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length
在真实的面试中遇到过这道题？

有道打麻将判断胡牌的题和这个很像...

"""

from collections import defaultdict

class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if (len(nums) % k) != 0:
            return False

        d = defaultdict(int)
        for i in nums:
            d[i] += 1

        for i in sorted(set(nums))[:-k + 1]:
            t = d[i]
            if d[i] > 0:
                # 把i ~ i+k的次数都减i出现的次数
                for j in range(k):
                    d[i + j] = d[i + j] - t
                    if d[i + j] < 0:
                        return False

        return all(x == 0 for x in d.values())
