# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode()
        dummy.next = head
        def reverseList(l):
            prev = None
            curr = l
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        def findMiddleOfList(l):
            slow = l
            fast = l
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        mid = findMiddleOfList(head)
        head2 = mid.next
        mid.next = None
        head2 = reverseList(head2)
        while head2:
            next = head.next
            next2 = head2.next
            head2.next = head.next
            head.next = head2
            head = next
            head2 = next2
        head = dummy.next