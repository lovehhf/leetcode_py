# -*- coding:utf-8 -*-

"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：
     5
    / \
   2   6
  / \
 1   3
示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true

提示：
数组长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """
        二叉搜索树性质: 左子树所有节点值 < 根节点, 根节点 < 所有右子树值, 左右子树都是二叉搜索树
        后续遍历: 左右根
        找出左子树的后续遍历序列和右子树的后续遍历序列, 递归左右子树
        :param postorder:
        :return:
        """
        if not postorder:
            return True
        l, r = [], []
        root = postorder[-1]
        n = len(postorder) - 1
        i = 0

        while (i < n):
            if postorder[i] >= root:
                break
            l.append(postorder[i])
            i += 1

        while (i < n):
            if postorder[i] < root:
                return False
            r.append(postorder[i])
            i += 1

        return self.verifyPostorder(l) and self.verifyPostorder(r)
