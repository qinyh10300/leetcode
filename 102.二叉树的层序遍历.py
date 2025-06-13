#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # 双数组写法
        # if root == None:
        #     return []
        # cur = [root]
        # ans = []
        # while cur:
        #     nxt = []
        #     vals = []
        #     for node in cur:
        #         vals.append(node.val)
        #         if node.left != None:
        #             nxt.append(node.left)
        #         if node.right != None:
        #             nxt.append(node.right)
        #     cur = nxt
        #     ans.append(vals)
        # return ans
    
        # 队列写法
        if root == None:
            return []
        ans = []
        q = deque([root])
        while q:
            vals = []
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                vals.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(vals)
        return ans
# @lc code=end

