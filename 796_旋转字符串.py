# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
给定两个字符串, A 和 B。

A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。

示例 1:
输入: A = 'abcde', B = 'cdeab'
输出: true

示例 2:
输入: A = 'abcde', B = 'abced'
输出: false
注意：

A 和 B 长度不超过 100。
"""


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A and not B:
            return True
        n = len(A)
        for i in range(n):
            if A[i:n] + A[:i] == B:
                return True
        return False

    def rotateString2(self, A, B):
        """
        使用额外空间
        """
        if not A and not B:
            return True
        n = len(A)
        A += A
        for i in range(n):
            if A[i:i + n] == B:
                return True
        return False

    def rotateString3(self, A, B):
        """
        和2一样
        :param A:
        :param B:
        :return:
        """
        return len(A)==len(B) and B in A+A