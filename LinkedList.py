class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, val):
        next_e = self
        while next_e.next is not None:
            next_e = next_e.next
        next_e.next = ListNode(val)

    def __str__(self):
        s = F"{self.val}"
        next_e = self.next
        while next_e is not None:
            s += F" -> {next_e.val}"
            next_e = next_e.next
        return s
