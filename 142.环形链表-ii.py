#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
# 链表的快慢指针问题

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return head
        return None
# @lc code=end

