# -*- coding:utf-8 -*-

"""
给你一个正方形字符数组 board ，你从数组最右下方的字符 'S' 出发。

你的目标是到达数组最左上角的字符 'E' ，数组剩余的部分为数字字符 1, 2, ..., 9 或者障碍 'X'。在每一步移动中，你可以向上、向左或者左上方移动，可以移动的前提是到达的格子没有障碍。

一条路径的 「得分」 定义为：路径上所有数字的和。

请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对 10^9 + 7 取余。

如果没有任何路径可以到达终点，请返回 [0, 0] 。



示例 1：

输入：board = ["E23","2X2","12S"]
输出：[7,1]
示例 2：

输入：board = ["E12","1X1","21S"]
输出：[4,2]
示例 3：

输入：board = ["E11","XXX","11S"]
输出：[0,0]


提示：

2 <= board.length == board[i].length <= 100

hard

加了各种限制的dp
"""

from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        dp[n - 1][n - 1][1] = 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X':
                    dp[i][j][1] = 0
                    continue
                for x, y in [(i + 1, j + 1), (i + 1, j), (i, j + 1)]:
                    if (0 <= x < n and 0 <= y < n and board[x][y] != 'X'):
                        t = int(board[i][j]) if (i != 0 or j != 0) else 0

                        # if (i == 4 and j == 4):
                        #     print(x, y, dp[x][y], t)

                        if (dp[x][y][0] + t > dp[i][j][0]):
                            dp[i][j][0] = dp[x][y][0] + t

                            if x == n - 1 and y == n - 1:
                                dp[i][j][1] = dp[x][y][1] + 1
                            else:
                                dp[i][j][1] = dp[x][y][1]

                        elif (dp[x][y][0] + t == dp[i][j][0]):
                            if x == n - 1 and y == n - 1:
                                dp[i][j][1] += 1
                            else:
                                dp[i][j][1] += dp[x][y][1]

        # for i in range(n):
        #     print(dp[i])

        if dp[0][0][1] == 0:
            return [0, 0]
        return [dp[0][0][0], dp[0][0][1] % (10 ** 9 + 7)]


s = Solution()
board = ["E999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
         "999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999S"]

print(s.pathsWithMaxScore(board))
