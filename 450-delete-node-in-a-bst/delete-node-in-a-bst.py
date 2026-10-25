# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        # # Picking the Inorder Predecessor and Adding the right sub tree to that
        # def helper(root):
        #     if not root.left:
        #         return root.right
        #     elif not root.right:
        #         return root.left
        #     rightchild = root.right
        #     lastright = rightmostNode(root.left)
        #     lastright.right = rightchild
        #     return root.left
        # def rightmostNode(root):
        #     while root.right:
        #         root = root.right
        #     return root
        # if not root:
        #     return
        # if root.val==key:
        #     return helper(root)
        # dummy = root
        # while root:
        #     if root.val>key:
        #         if root.left and root.left.val==key:
        #             root.left = helper(root.left)
        #             break
        #         else:
        #             root = root.left
        #     else:
        #         if root.right and root.right.val==key:
        #             root.right = helper(root.right)
        #             break
        #         else:
        #             root = root.right
        # return dummy

        if not root:
            return
        
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right,temp.val)
        return root