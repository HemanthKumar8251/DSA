# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # # Get the In-Order Traversal and then use 2 Pointers
        # res = []
        # st = []
        # # In-Order Traversal
        # while st or root:
        #     while root:
        #         st.append(root)
        #         root = root.left
        #     root = st.pop()
        #     res.append(root.val)
        #     root = root.right

        # low,high = 0,len(res)-1

        # while low<high:
        #     if res[low]+res[high]>k:
        #         high-=1
        #     elif res[low]+res[high]<k:
        #         low+=1
        #     else:
        #         return True
        # return False

        # # Using 2 In-order traversal (Standard and Reverse) to use the 2-Pointers directly on the Tree
        # class BSTIterator:
        #     def __init__(self,root, reverse_true):
        #         self.st = []
        #         self.reverse_true = reverse_true
        #         self._push_all(root)
            
        #     def has_next(self):
        #         return len(self.st)>0

        #     def next(self):
        #         node = self.st.pop()
        #         if self.reverse_true:
        #             self._push_all(node.left)
        #         else:
        #             self._push_all(node.right)
        #         return node.val

        #     def _push_all(self,node):
        #         while node:
        #             self.st.append(node)
        #             node = node.right if self.reverse_true else node.left

        # left_iter = BSTIterator(root,False)
        # right_iter = BSTIterator(root,True)

        # low = left_iter.next()
        # high = right_iter.next()

        # while low<high:
        #     curr_sum = low+high
        #     if curr_sum == k:
        #         return True
        #     elif curr_sum<k:
        #         low = left_iter.next()
        #     else:
        #         high = right_iter.next()
            
        # return False

        # Using Hash Map and BFS
        seen = set()
        q = deque([root])
        while q:
            x = q.popleft()
            if not x:
                continue
            if k-x.val in seen:
                return True
            else:
                seen.add(x.val)
            q.append(x.left)
            q.append(x.right)
        return False