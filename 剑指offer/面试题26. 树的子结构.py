# -*- coding:utf-8 -*-

"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：
0 <= 节点个数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, A, B):
        """
        判断 B 是否是 A 的根节点相同的子结构
        :param A:
        :param B:
        :return:
        """
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.dfs(A.left, B.left) and self.dfs(A.right, B.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        if self.dfs(A, B):
            return True
        # 递归 A 的左右子树
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
