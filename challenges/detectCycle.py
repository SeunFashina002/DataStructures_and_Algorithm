# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # O(n) time | O(1) space
    def detectCycle(self, head):
        if not head:
            return None

        slow, fast = head, head
        cycle = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                cycle = True
                break
        
        if not cycle:
            return None
        
        start = head
        while start != slow:
            start = start.next
            slow = slow.next
        
        return start