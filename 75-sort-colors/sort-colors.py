class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num]+=1
        j = 0
        for i in range(len(nums)):
            while j not in hash_map:
                j+=1
            nums[i]=j
            hash_map[j]-=1
            if hash_map[j]==0:
                j+=1