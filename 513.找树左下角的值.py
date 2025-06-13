#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        node = None
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
        return node.val  # 最后遍历到的节点
# @lc code=end

