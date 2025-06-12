#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def f(left_node, right_node):
            if left_node == None or right_node == None:
                return left_node == right_node
            return left_node.val == right_node.val and f(left_node.left, right_node.right) and f(left_node.right, right_node.left)
        return f(root.left, root.right)
# @lc code=end

