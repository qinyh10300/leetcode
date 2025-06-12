#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def f(node, cnt=0):
            if node == None:
                return
            if cnt == len(ans):
                ans.append(node.val)
            f(node.right, cnt+1)
            f(node.left, cnt+1)
        f(root)
        return ans
# @lc code=end

