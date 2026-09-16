class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        greater_ele = [-1]*len(nums)
        mst = []
        n = len(nums)
        for i in range(2*n):
            while mst and nums[i%n]>nums[mst[-1]]:
                greater_ele[mst.pop()] = nums[i%n]
            mst.append(i%n)
        return greater_ele