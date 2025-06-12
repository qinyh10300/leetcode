#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = -inf  # 中序遍历时使用
    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        # # 前序遍历
        # if root == None:
        #     return True
        # x = root.val
        # return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)

        # # 中序遍历
        # if root == None:
        #     return True
        # if not self.isValidBST(root.left):
        #     return False
        # if root.val <= self.pre:
        #     return False
        # self.pre = root.val
        # if not self.isValidBST(root.right):
        #     return False
        # return True
        # # return self.isValidBST(root.right)

        # 后序遍历（复杂一点）
        def f(node):
            if node == None:
                return inf, -inf
            left_low, left_high = f(node.left)
            right_low, right_high = f(node.right)
            x = node.val
            if x > left_high and x < right_low:
                return min(left_low, x), max(right_high, x)
            else:
                return -inf, inf
        return f(root)[1] != inf
# @lc code=end

