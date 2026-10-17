# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        # Using DFS Approch
        def dfs(root,level):
            if not root:
                return level-1
            max_depth = max(dfs(root.left,level+1),dfs(root.right,level+1))
            return max_depth
        return dfs(root,1)