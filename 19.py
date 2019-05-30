# https://leetcode.com/submissions/detail/232210244/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        t = head
        count = 0
        while t is not None:
            count += 1
            t = t.next
        t = head
        count -= (1 + n)
        if count >= 0:
            for _ in range(count):
                t = t.next
            t.next = t.next.next
        else:
            head = head.next
        return head

