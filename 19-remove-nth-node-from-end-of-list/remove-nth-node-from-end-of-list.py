# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # # Using 2-pointers, slow and fast pointer
        # dummy = ListNode(next=head)
        # fast = dummy
        # slow = dummy
        # for _ in range(n+1):
        #     fast = fast.next
        # while fast:
        #     slow = slow.next
        #     fast = fast.next
        # slow.next = slow.next.next
        # return dummy.next

        # Finding the length of LL and removing the lenght-n element
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        if length==n:
            head = head.next
            return head
        prev = head
        for _ in range(length-n-1):
            prev = prev.next
        prev.next = prev.next.next
        return head