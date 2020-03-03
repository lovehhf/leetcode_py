# -*- coding:utf-8 -*-

"""
给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。

每一步，你可以从下标 i 跳到下标：
i + 1 满足：i + 1 < arr.length
i - 1 满足：i - 1 >= 0
j 满足：arr[i] == arr[j] 且 i != j

请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。
注意：任何时候你都不能跳到数组外面。

示例 1：
输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
输出：3
解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。

示例 2：
输入：arr = [7]
输出：0
解释：一开始就在最后一个元素处，所以你不需要跳跃。

示例 3：
输入：arr = [7,6,9,6,9,6,9,7]
输出：1
解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。

示例 4：
输入：arr = [6,1,9]
输出：2

示例 5：
输入：arr = [11,22,7,7,7,7,7,7,7,22,13]
输出：3

提示：
1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from collections import defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        bfs最短路问题, 搜索下一步可以跳跃的路径, 直到搜索到 n - 1
        用字典保存相同的值的下标
        :param arr:
        :return:
        """
        d = defaultdict(list)
        n = len(arr)

        for i in range(n):
            d[arr[i]].append(i)

        vis = [0] * n
        vis[0] = 1
        q = [(0, 0)]
        while q:
            i, k = q.pop(0)
            for j in d[arr[i]] + [i - 1, i + 1]:
                if j < 0 or j >= n or vis[j]:
                    continue
                if j == n - 1:
                    return k + 1
                vis[j] = 1
                q.append((j, k + 1))
            d[arr[i]] = []  # 非常重要, 不然会超时

        return 0
