class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hash_map and hash_map[diff]!=i:
                return [i,hash_map[diff]]
        return