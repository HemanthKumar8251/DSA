class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        cur_arr = []
        seen = [False]*n
        nums.sort()
        def permutations():
            if len(cur_arr)==n:
                result.append(list(cur_arr))
                return
            for i in range(n):
                if seen[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not seen[i - 1]:
                    continue
                seen[i]=True
                cur_arr.append(nums[i])
                permutations()
                cur_arr.pop()
                seen[i]=False
        
        permutations()
        return result