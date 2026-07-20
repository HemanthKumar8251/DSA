class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = 1
        max_prod1, max_prod2 = -inf,-inf
        for i in range(len(nums)):
            max_prod1 = max(max_prod1, prod := prod*nums[i])
            if prod == 0:
                prod = 1
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            max_prod2 = max(max_prod2, prod := prod*nums[i])
            if prod == 0:
                prod = 1
        return max(max_prod1,max_prod2)