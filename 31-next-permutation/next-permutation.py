class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        indx_i=indx_j=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                indx_i = i
                break
        if indx_i == -1:
            nums.sort()
            return
        for j in range(n-1,-1,-1):
            if nums[indx_i]<nums[j]:
                indx_j = j
                break
        nums[indx_i],nums[indx_j] = nums[indx_j],nums[indx_i]
        nums[indx_i+1:]= sorted(nums[indx_i+1:]) 
        
        