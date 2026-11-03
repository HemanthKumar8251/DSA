# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        # Using In-Order Traversal
        st = []
        res = []
        min_diff =1000000
        while st or root:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            if res:
                min_diff = min(min_diff,root.val-res.pop())
            res.append(root.val)
            root = root.right
        return min_diff