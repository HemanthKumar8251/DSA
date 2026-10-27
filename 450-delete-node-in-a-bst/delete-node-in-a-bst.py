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

        # # Recursive approach for replacing the val and deleting the node
        # if not root:
        #     return
        
        # if root.val > key:
        #     root.left = self.deleteNode(root.left,key)
        # elif root.val < key:
        #     root.right = self.deleteNode(root.right,key)
        # else:
        #     if root.left is None:
        #         return root.right
        #     if root.right is None:
        #         return root.left

        #     temp = root.right
        #     while temp.left:
        #         temp = temp.left
        #     root.val = temp.val
        #     root.right = self.deleteNode(root.right,temp.val)
        # return root

        # Iterative approach for deletion by replacing the node val
        curr = root
        prev = None
        # Step 1: Finding the target node
        while curr and curr.val!=key:
            prev = curr
            if curr.val>key:
                curr = curr.left
            elif curr.val< key:
                curr = curr.right
        # If the key doesn't exist in the BST
        if not curr:
            return root

        # Step 2: Handling the deletion according to number of child nodes
        # Case 1 : The node has 2 child nodes
        if curr.left and curr.right:
            succ_parent = curr
            succ = curr.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            curr.val = succ.val
            curr = succ
            prev = succ_parent
        # Case 2 : The node has 0(leaf) or 1 child node
        child = curr.left if curr.left else curr.right

        # Root node deletion
        if not prev:
            return child

        if prev.left == curr:
            prev.left = child
        if prev.right == curr:
            prev.right = child

        return root