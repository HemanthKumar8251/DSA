# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # Using the in-order traversal
        count = 0
        st = []
        while (st or root) and count<k:
            while root:
                st.append(root)
                root = root.left
            count +=1
            root = st.pop()
            smallest = root.val
            root = root.right 
        return smallest