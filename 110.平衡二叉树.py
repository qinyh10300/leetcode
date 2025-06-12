#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def f(node):
            if node == None:
                return 0
            left_height = f(node.left)
            if left_height == -1:
                return -1
            # else:
            #     left_height += 1
            # 在return的时候+1了
            right_height = f(node.right)
            if right_height == -1:
                return -1
            # else:
            #     right_height += 1
            # 在return的时候+1了
            if abs(left_height-right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return False if f(root) == -1 else True 
# @lc code=end

