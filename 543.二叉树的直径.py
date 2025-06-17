#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # # 方法一
        # ans = 0
        # def dfs(node):
        #     if node == None:
        #         return -1   # 注意这里是返回-1，才是正确的。可以通过推导叶节点递归来确定
        #     nonlocal ans
        #     left_height = dfs(node.left) + 1
        #     right_height = dfs(node.right) + 1
        #     ans = max(ans, left_height + right_height)
        #     return max(left_height, right_height)
        # dfs(root)
        # return ans

        # 方法二（略有差别）
        ans = 0
        def dfs(node):
            if node == None:
                return -1
            nonlocal ans
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            ans = max(ans, left_height + right_height + 2)
            return max(left_height, right_height) + 1
        dfs(root)
        return ans
# @lc code=end

