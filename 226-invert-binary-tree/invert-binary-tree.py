# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        # # Iterative BFS approach
        # if not root:
        #     return
        # q = deque()
        # q.append(root)
        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #         node.right,node.left = node.left, node.right
        # return root

        # Iterative DFS
        if not root:
            return
        st = [root]
        while st:
            node = st.pop()
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
            node.right,node.left = node.left,node.right
        return root