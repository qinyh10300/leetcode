#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        len = 0
        while cur:
            len += 1
            cur = cur.next

        dummy = ListNode(next=head)
        p0 = dummy
        cur = head
        pre = None
        while k <= len:
            # 尽量使用这种反转方法
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            # 把这些赋值操作都当成值传递，而不是引用传递吧
            nxt = p0.next
            p0.next.next = cur
            # 上面两句话的顺序不影响结果，只是因为nxt.next在后续会统一更改
            p0.next = pre
            p0 = nxt
            len -= k
        return dummy.next
# @lc code=end

