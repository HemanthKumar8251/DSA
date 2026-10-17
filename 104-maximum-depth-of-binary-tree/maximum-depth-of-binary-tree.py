# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        # # Using Recursive Top Down DFS Approch
        # def dfs(root,level):
        #     if not root:
        #         return level
        #     max_depth = max(dfs(root.left,level+1),dfs(root.right,level+1))
        #     return max_depth
        # return dfs(root,0)

        # # Using Recursive Bottom Up DFS Approach
        # if not root:
        #     return 0
        
        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)

        # return 1+max(left_depth,right_depth)

        # Iterative DFS Approach
        max_depth = 0
        if not root:
            return max_depth
        st = [(root,1)]
        while st:
            node,depth = st.pop()
            max_depth = max(depth,max_depth)
            if node.right:
                st.append((node.right,depth+1))
            if node.left:
                st.append((node.left,depth+1))
        return max_depth