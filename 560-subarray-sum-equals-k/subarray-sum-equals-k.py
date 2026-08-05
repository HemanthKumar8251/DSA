class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        
        # O(n**2) TLE, O(1)
        # for i in range(n):
        #     sum = 0
        #     for j in range(i,n):
        #         sum += nums[j]
        #         if sum==k:
        #             count+=1

        # O(n) Time, O(n) Space
        current_sum = 0
        count = 0
        prefix_seen = {0:1}
        for num in nums:
            current_sum += num
            diff = current_sum - k
            if diff in prefix_seen:
                count += prefix_seen[diff]
            prefix_seen[current_sum] = prefix_seen.get(current_sum,0)+1
        return count