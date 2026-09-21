# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # carry = 0
        # dummy = ListNode()
        # prev = dummy
        # while l1 and l2:
        #     node = ListNode(val=(l1.val+l2.val+carry)%10)
        #     carry = (l1.val+l2.val+carry)//10
        #     prev.next = node
        #     prev = node
        #     l1 = l1.next
        #     l2 = l2.next
        # while l1 and carry==1:
        #     node = ListNode(val=(l1.val+carry)%10)
        #     carry = (l1.val+carry)//10
        #     prev.next = node
        #     prev = node
        #     l1 = l1.next
        # while l2 and carry==1:
        #     node = ListNode(val=(l2.val+carry)%10)
        #     carry = (l2.val+carry)//10
        #     prev.next = node
        #     prev = node
        #     l2 = l2.next
        # if l1:
        #     prev.next = l1
        # if l2:
        #     prev.next = l2
        # if carry == 1:
        #     prev.next = ListNode(val=1)
        # return dummy.next

        carry = 0
        dummy = ListNode()
        prev = dummy
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total%10
            carry = total//10
            node = ListNode(val=num)
            prev.next = node
            prev = node
            
        return dummy.next