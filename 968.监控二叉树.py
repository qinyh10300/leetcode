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
            # return 这个节点的父节点安放摄像头（黄色节点）  这个节点安放摄像头（蓝色节点）  这个节点的子节点安放摄像头（红色节点）
            if node == None:
                return 0, inf, 0
            left_fa, left, left_ch = dfs(node.left)
            right_fa, right, right_ch = dfs(node.right)
            return  min(left, left_ch) + min(right, right_ch), 
                    min(left_fa, left, left_ch) + min(right_fa, right, right_ch) + 1, 
                    min(left + right, left + right_ch, left_ch + right)
        return min(dfs(root)[1:])
    
        # 如果不是二叉树的情况，那么红色节点的计算就变得麻烦，枚举的情况太多，但是可以用下面的方法优化问题：（以三个节点的情况为例）
        # 黄色 = min(蓝1, 红1) + min(蓝2, 红2) + min(蓝3, 红3)
        # 红色 = 黄色 + max(0, min(蓝1 - 红1, 蓝2 - 红2, 蓝3 - 红3))  ->  相当于找了(蓝1, 红2, 红3)之类且除去(红1, 红2, 红3)的排列组合最小值
        # 蓝色 = min(蓝1, 红1, 黄1) + min(蓝2, 红1, 黄2) + min(蓝3, 红1, 黄3) + cost[i]
# @lc code=end

