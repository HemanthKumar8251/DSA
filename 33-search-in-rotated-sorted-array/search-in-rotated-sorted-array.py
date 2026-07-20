class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        while left<=right:
            mid = left + (right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[left]:
                # Left-side is sorted
                if nums[mid]>target and nums[left]<=target:
                    # Moving to the left half
                    right = mid - 1
                else:
                    # Moving right
                    left = mid + 1
            else:
                # Right-side is sorted
                if nums[mid]<target and nums[right]>=target:
                    # Moving right
                    left = mid + 1
                else:
                    # Moving to the left half
                    right = mid - 1
        return -1