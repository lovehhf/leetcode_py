# -*- coding:utf-8 -*-


"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

提示：
1 <= board.length <= 200
1 <= board[i].length <= 200

注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

bfs 超时
"""

from typing import List


class Solution:

    def dfs(self, m, n, i, j, word, k, vis, board):
        # print(i, j, board[i][j], vis)
        if k == len(word) - 1:
            return True
        ds = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        for dx, dy in ds:
            x = i + dx
            y = j + dy
            if (0 <= x < m and 0 <= y < n and not vis[x][y] and word[k + 1] == board[x][y]):
                vis[x][y] = 1
                if self.dfs(m, n, x, y, word, k + 1, vis, board):
                    return True
                vis[x][y] = 0
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        vis = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):

                vis[i][j] = 1
                if word[0] == board[i][j] and self.dfs(m, n, i, j, word, 0, vis, board):
                    return True
                vis[i][j] = 0

        return False


board = [["A", "B", "C", "E"],
         ["S", "F", "E", "S"],
         ["A", "D", "E", "E"]]
word = "ABCESEEEFS"
s = Solution()
print(s.exist(board, word))
