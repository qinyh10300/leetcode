#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # return 这个节点的父节点安放摄像头  这个节点安放摄像头  这个节点的子节点安放摄像头 
            if node == None:
                return 0, inf, 0
            left_fa, left, left_ch = dfs(node.left)
            right_fa, right, right_ch = dfs(node.right)
            return  min(left, left_ch) + min(right, right_ch), 
                    min(left_fa, left, left_ch) + min(right_fa, right, right_ch) + 1, 
                    min(left + right, left + right_ch, left_ch + right)
        return min(dfs(root)[1:])
# @lc code=end

