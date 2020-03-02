"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
 and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

from LinkedList import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        current = result = ListNode(0)
        previous = None
        while p1 or p2 :
            m_sum = (p1.val if p1 else 0) + (p2.val if p2 else 0) + current.val
            current.val = m_sum % 10
            current.next = ListNode(int(m_sum / 10))
            previous = current
            current = current.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        if previous.next.val == 0:
            previous.next = None
        return result


def g_print(l: ListNode) -> None:
    while l is not None:
        print(l.val, " " if l.next is None else " -> ", end='')
        l = l.next
    print("")


l1 = ListNode(5)
l2 = ListNode(5)
print(l1)
print(l2)
print(Solution().addTwoNumbers(None, l2))
# print(None + None)
#
