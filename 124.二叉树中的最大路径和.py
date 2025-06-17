#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(node):
            if node == None:
                return 0
            nonlocal ans
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            ans = max(ans, left_sum + right_sum + node.val)
            return max(max(left_sum, right_sum) + node.val, 0)    # 因为这个节点的值可能是一个很大的负数，所以需要和 0 取一个最大值
        dfs(root)
        return ans
# @lc code=end

