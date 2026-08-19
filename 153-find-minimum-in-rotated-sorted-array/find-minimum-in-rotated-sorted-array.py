class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid = left + (right-left)//2
            if nums[mid]>nums[-1]:
                # Move to the right as left is sorted
                left = mid+1
            else:
                # Move to the left as right is sorted
                right = mid-1
        return nums[left]

        # Using bisect_left function
        # return nums[bisect_left(nums, True, key=lambda n: n <= nums[-1])]