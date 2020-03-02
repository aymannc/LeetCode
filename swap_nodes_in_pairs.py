from LinkedList import ListNode


class Solution:
    def swap_pairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        element = head
        head = head.next
        prev = None
        while element is not None:
            next_e = element.next
            if next_e is not None:
                element.next = next_e.next
                next_e.next = element
                if prev is not None:
                    prev.next = next_e
            prev = element
            element = element.next

        return head

    def swap_pairs2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        element = head
        new_head = []
        while element is not None:
            if element.next:
                new_head.append(element.next.val)
            new_head.append(element.val)
            try:
                element = element.next.next
            except:
                element = element.next

        return new_head

    # def swap_pairs_data(self, head: ListNode) -> ListNode:
    #     if head is None or head.next is None:
    #         return head
    #     element = head
    #     while element is not None and element.next is not None:
    #         tmp = element.val
    #         element.val = element.next.val
    #         element.next.val = tmp
    #         element = element.next.next
    #     # return head

linked_list = ListNode(1)
linked_list.add(ListNode(2))
linked_list.add(ListNode(3))
linked_list.add(ListNode(4))
linked_list.add(ListNode(5))
# linked_list.add(ListNode(6))
print(linked_list)
linked_list2 = Solution().swap_pairs(linked_list)
print(linked_list2)
