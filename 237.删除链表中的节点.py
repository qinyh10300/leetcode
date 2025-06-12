#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 脑筋急转弯，能够利用O(1)的时间进行删除节点
        # 将这个节点变成它后面的那个节点，再把后面的那个节点删除即可
        node.val = node.next.val
        node.next = node.next.next
# @lc code=end

