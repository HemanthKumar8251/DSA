# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        # # Using BFS
        # res = []
        # if not root:
        #     return res
        # q = deque()
        # q.append(root)
        # while q:
        #     curr_level = []
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         curr_level.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     res.append(curr_level)
        # return res

        # DFS
        
        def helper_fun(node,level,res):
            if not node:
                return
            
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            helper_fun(node.left,level+1,res)
            helper_fun(node.right,level+1,res)

        res = []
        helper_fun(root,0,res)
        return res