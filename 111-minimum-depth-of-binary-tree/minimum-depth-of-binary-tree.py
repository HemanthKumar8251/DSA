# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        level = 1
        # Using BFS
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node.right and not node.left:
                    return level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1