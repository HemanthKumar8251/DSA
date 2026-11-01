# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        # Recursively building the tree with the mid element of the range
        def helper(left,right):
            if left>right:
                return None
            mid = (right+left)//2
            node = TreeNode(nums[mid])
            node.left = helper(left,mid-1)
            node.right = helper(mid+1,right)
            return node
        return helper(0,len(nums)-1)