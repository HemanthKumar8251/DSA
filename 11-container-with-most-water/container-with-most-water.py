class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_capacity = -inf
        n = len(height)
        left,right = 0,n-1
        while left<right:
            max_capacity = max(max_capacity,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return max_capacity