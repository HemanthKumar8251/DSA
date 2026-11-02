# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        # # Using In-Order Traversal of the BST
        # range_sum = 0
        # st = []
        # while st or root:
        #     while root:
        #         st.append(root)
        #         root = root.left
        #     root = st.pop()
        #     if root.val>high:
        #         break
        #     elif root.val>=low:
        #         range_sum+=root.val
        #     root = root.right
        # return range_sum

        # Recursive smart traversal approach
        def bst(root):
            if root is None:
                return 0
            if root.val<low:
                return bst(root.right)
            if root.val>high:
                return bst(root.left)
            return root.val+bst(root.left)+bst(root.right)
        return bst(root)