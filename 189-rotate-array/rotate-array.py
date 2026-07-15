class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k==l:
            return
        if k>l:
            k%=l
        temp = copy.deepcopy(nums)
        for i in range(k):
            nums[i] = temp[l-k+i]
        for j in range(k,l):
            nums[j] = temp[j-k]