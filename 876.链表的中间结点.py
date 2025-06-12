#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
# 链表的**快慢指针**问题

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
# @lc code=end

