# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        # # Using Bottom-Up Recursive DFS
        # if not root:
        #     return 0

        # left_height = self.minDepth(root.left)
        # right_height = self.minDepth(root.right)

        # if not root.left and not root.right:
        #     return 1
        
        # if not root.left:
        #     return 1+right_height

        # if not root.right:
        #     return 1+left_height

        # return 1+min(left_height,right_height)

        # Using BFS
        if not root:
            return 0
        level = 1
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