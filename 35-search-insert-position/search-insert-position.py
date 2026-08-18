class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # O(n) Time Complexity, List Traversal
        for i,num in enumerate(nums):
            if num>=target:
                return i
        return len(nums)

        # O(log n) Time Complexity, Using Binary Search
        i,j=0,len(nums)-1
        while i<j:
            mid = (i+j)//2
            if nums[mid]<target:
                i=mid+1
            elif nums[mid]>target:
                j=mid-1
            else:
                return mid
        return len(nums)