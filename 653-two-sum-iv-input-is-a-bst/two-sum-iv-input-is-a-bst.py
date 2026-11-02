# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Get the In-Order Traversal and then use 2 Pointers
        res = []
        st = []
        # In-Order Traversal
        while st or root:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            res.append(root.val)
            root = root.right
            
        low,high = 0,len(res)-1

        while low<high:
            if res[low]+res[high]>k:
                high-=1
            elif res[low]+res[high]<k:
                low+=1
            else:
                return True
        return False
