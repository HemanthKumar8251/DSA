class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash_map = {}
        # for i in range(len(nums)):
        #     hash_map[nums[i]] = i
        # for i in range(len(nums)):
        #     diff = target-nums[i]
        #     if diff in hash_map and hash_map[diff]!=i:
        #         return [i,hash_map[diff]]

        # 2-Pointer Approach
        enumerated_nums = [(num,i) for i,num in enumerate(nums)]
        enumerated_nums.sort(key=lambda x: x[0])
        i = 0
        j = len(nums)-1
        while i<j:
            cur_sum = enumerated_nums[i][0]+enumerated_nums[j][0]
            if cur_sum<target:
                i+=1
            elif cur_sum>target:
                j-=1
            else:
                return [enumerated_nums[i][1],enumerated_nums[j][1]]