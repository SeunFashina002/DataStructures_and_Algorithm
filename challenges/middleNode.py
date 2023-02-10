# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        res = head
        l = 0
        while head:
            head = head.next
            l += 1
        mid = l//2
        while mid:
            res = res.next
            mid -= 1
        return res