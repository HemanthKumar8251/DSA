class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # O(nlogn) Time, O(1) Space
        # nums.sort()
        # count = 1
        # max_count = 1
        # for i in range(1,len(nums)):
        #     if nums[i]-1==nums[i-1]:
        #         count += 1
        #     elif nums[i]==nums[i-1]:
        #         continue
        #     else:
        #         max_count = max(max_count,count)
        #         count = 1
        # max_count = max(max_count,count)
        # return max_count

        # Using O(n) Time, O(n) Space
        count = 0
        max_count=0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                count = 1
                num+=1
                while num in nums:
                    count+=1
                    num+= 1
                max_count = max(max_count,count)
        return max_count
        