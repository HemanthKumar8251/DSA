# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return TreeNode(val)
        curr = root
        prev = None
        while curr:
            prev = curr
            if curr.val>val:
                curr = curr.left
            elif curr.val<val:
                curr = curr.right
        if prev.val<val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
        return root