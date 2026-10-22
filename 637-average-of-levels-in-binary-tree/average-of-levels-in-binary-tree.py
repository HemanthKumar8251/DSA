# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        # Using BFS
        q = deque([root])
        averages = []
        level = 0
        while q:
            total = 0
            node_count = 0
            for _ in range(len(q)):
                node = q.popleft()
                node_count += 1
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            averages.append(total/node_count)
        return averages