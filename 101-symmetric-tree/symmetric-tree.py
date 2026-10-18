# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        # # Recursive Approach
        # def symmetric(n1,n2):
        #     if not n1 and not n2:
        #         return True
        #     if not n1 or not n2 or n1.val!=n2.val:
        #         return False
        #     return symmetric(n1.left,n2.right) and symmetric(n1.right,n2.left)
        # return symmetric(root.left,root.right)

        # Iterative Approach
        q = deque([root.left,root.right])
        while q:
            n1 = q.popleft()
            n2 = q.popleft()

            if not n1 and not n2:
                continue

            if not n1 or not n2 or n1.val!=n2.val:
                return False

            q.append(n1.left)
            q.append(n2.right)
            q.append(n1.right)
            q.append(n2.left)

        return True

            