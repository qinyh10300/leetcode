#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        left_val = min(p.val, q.val)
        right_val = max(p.val, q.val)
        def lca(node):
            if node.val < left_val:
                return lca(node.right)
            elif node.val > right_val:
                return lca(node.left)
            else:
                return node
        return lca(root)
# @lc code=end

