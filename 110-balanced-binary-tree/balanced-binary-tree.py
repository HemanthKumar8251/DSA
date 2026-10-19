# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        # # Recursive Top Down Approach Time : O(N^2) as we re-calculate the height every time
        # if not root:
        #     return True
        # def height(node):
        #     if not node:
        #         return 0
        #     return max(height(node.left),height(node.right)) + 1
        # if abs(height(root.left)-height(root.right))>1:
        #     return False
        # return self.isBalanced(root.left) and self.isBalanced(root.right)

        # Recursive Bottom Up Approach
        if not root:
            return True
        def helper(node):
            if not node:
                return 0
            left_h = helper(node.left)
            if left_h==-1:
                return -1
            right_h = helper(node.right)
            if right_h==-1:
                return -1
            if abs(left_h-right_h)>1:
                return -1
            return 1+max(left_h,right_h)
        return helper(root)!=-1

        # Post Order Iterative Approach

        