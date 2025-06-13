#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
# LCA要熟练

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node):
            if node == q or node == p or node == None:
                return node
            left_node = lca(node.left)
            right_node = lca(node.right)
            if left_node == None and right_node == None:
                return None
            elif left_node != None and right_node != None:
                return node
            else:
                return right_node if left_node == None else left_node
        return lca(root)
# @lc code=end

