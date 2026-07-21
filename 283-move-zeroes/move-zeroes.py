class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i=0
        # j = i+1
        # n = len(nums)
        # while i<n and j<n:
        #     while i<n and nums[i]!=0:
        #         i+=1
        #     j = i+1
        #     while j<n and nums[j]==0:
        #         j+=1
        #     if i<n and j<n:
        #         nums[i],nums[j] = nums[j],nums[i]
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            