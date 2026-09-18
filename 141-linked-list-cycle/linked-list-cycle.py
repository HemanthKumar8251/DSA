# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # # Using the hash set
        # seen = set()
        # curr = head
        # while curr:
        #     if curr in seen:
        #         return True
        #     seen.add(curr)
        #     curr = curr.next
        # return False

        # Using 2-pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:
                return True
        return False