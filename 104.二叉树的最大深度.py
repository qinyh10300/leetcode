#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # 方法一，深度从底层往上传递
        # if root == None:
        #     return 0
        # left_height = self.maxDepth(root.left)
        # right_height = self.maxDepth(root.right)
        # return max(left_height, right_height) + 1

        # 方法二，深度从顶层往下传递
        ans = 0
        def f(node, cnt=0):
            nonlocal ans
            if node == None:
                ans = max(ans, cnt)
                return
            f(node.left, cnt+1)
            f(node.right, cnt+1)
        f(root)
        return ans
# @lc code=end

