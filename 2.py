# https://leetcode.com/submissions/detail/230411556/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        i = 0
        a = l1
        while a is not None:
            num1 += (a.val * (10 ** i))
            i += 1
            a = a.next
        num2 = 0
        i = 0
        a = l2
        while a is not None:
            num2 += (a.val * (10 ** i))
            i += 1
            a = a.next
        ans = str(num1 + num2)
        ans = ans[::-1]
        ans_node = None
        prev = None
        for n in ans:
            node = ListNode(int(n))
            if ans_node is None:
                ans_node = node
            else:
                prev.next = node
            prev = node
        return ans_node

