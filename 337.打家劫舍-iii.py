#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # return 选node情况的最大值 不选node情况的最大值
            if node == None:
                return -inf, 0
            left_with, left_without = dfs(node.left)
            right_with, right_without = dfs(node.right)
            return right_without + left_without + node.val, max(left_with, left_without) + max(right_with, right_without)
        return max(dfs(root))
# @lc code=end

