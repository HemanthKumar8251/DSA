# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        # # Using BFS
        # q = deque([root])
        # averages = []
        # while q:
        #     total = 0
        #     level_size = len(q)
        #     for _ in range(level_size):
        #         node = q.popleft()
        #         total += node.val
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     averages.append(total/level_size)
        # return averages

        # Using Recursive DFS
        levels = []
        def helper(node,level,levels):
            if not node:
                return
            if level==len(levels):
                levels.append([])
            levels[level].append(node.val)
            helper(node.left,level+1,levels)
            helper(node.right,level+1,levels)
        helper(root,0,levels)
        return [sum(x)/len(x) for x in levels]