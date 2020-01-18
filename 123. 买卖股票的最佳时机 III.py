# -*- coding:utf-8 -*-

"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

dp[i][j][0/1]: 第 i 天, 最多还可以进行进行 j 次交易, 手上是否持有股票

状态转移方程:
dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

注意需要在买入的时候算交易次数(dp[i - 1][j - 1][1]), 不能在卖的时候才算交易次数(dp[i - 1][j - 1][1]),
否则会出现最后手上还有股票的情况

初始状态:
dp[0][j][0] = 0
dp[0][j][1] 不存在
dp[i][0][1] 不存在

答案就是：dp[n][2][0]

根据状态转移方程要求 dp[i][2][0] 和 dp[i][2][1], 那么肯定就要先求出 dp[i - 1][1][1] 或 dp[i - 1][1][0]
求 p[i - 1][1][1] 和 dp[i - 1][1][0] 可以用 121 题中的方法
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[[0, 0] for _ in range(3)] for _ in range(n + 1)]
        prices = [0] + prices

        # 初始状态, i = 1 时, dp[0][j][1]这种情况不存在, dp[1][j][1] = -prices[1]
        for j in range(1, 3):
            dp[1][j][1] = -prices[1]

        # 先求出状态 j = 1 的所有情况, 才能去更新 j = 2 的情况
        for j in range(1, 3):
            for i in range(2, n + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[n][2][0]

s = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(s.maxProfit(prices))
