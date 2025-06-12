#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
# 双指针问题

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 寻找链表中点
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 翻转链表右半边
        pre = None
        while slow:
            nxt = slow.next
            slow.next = pre
            pre = slow
            slow = nxt

        left = head
        right = pre
        # 交叉重排
        while right.next:    # 这个判断条件需要手推一遍
            left_nxt = left.next
            right_nxt = right.next
            left.next = right
            right.next = left_nxt

            left = left_nxt
            right = right_nxt
# @lc code=end

