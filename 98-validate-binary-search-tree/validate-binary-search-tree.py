# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        # # Iterative BFS Approach
        # q = deque([(root,float('-inf'),float('inf'))])
        # while q:
        #     for _ in range(len(q)):
        #         node,low,high = q.popleft()
        #         if not (low<node.val<high):
        #             return False
        #         if node.left:  
        #             q.append((node.left,low,node.val))
        #         if node.right:
        #             q.append((node.right,node.val,high))
        # return True

        # # Recursive DFS Approach
        # def traversal(node,low,high):
        #     if not node:
        #         return True
        #     if not (low<node.val<high):
        #         return False
        #     return traversal(node.right,node.val,high) and traversal(node.left,low,node.val)
        # return traversal(root,float('-inf'),float('inf'))

        # Iterative DFS Approach
        st = []
        prev = None
        while st or root:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            if prev and root.val<=prev.val:
                return False
            prev = root
            root = root.right
        return True