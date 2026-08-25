class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        cur_arr = []
        used = defaultdict(bool)
        nums.sort()
        def permutations():
            if len(cur_arr)==n and cur_arr not in result:
                result.append(list(cur_arr))
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i]=True
                cur_arr.append(nums[i])
                permutations()
                cur_arr.pop()
                used[i]=False
        
        permutations()
        return result