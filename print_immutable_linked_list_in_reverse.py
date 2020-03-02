"""
Print out an immutable singly linked list in reverse in linear time (O(n)) and less than linear space (space<(O(n))

for example :

Given the linked list : 4-5-12-1-3
Your program should print : 3-1-12-5-4
"""
from LinkedList import ListNode


class Solution:
    @staticmethod
    def print_linked_list(head: ListNode) -> None:
        if head is None:
            return
        Solution.print_linked_list(head.next)
        print(head.val, end=' -> ')


linked_list = ListNode(4)
linked_list.add(ListNode(5))
linked_list.add(ListNode(12))
linked_list.add(ListNode(1))
linked_list.add(ListNode(3))
print(linked_list)
Solution.print_linked_list(linked_list)
