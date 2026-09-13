class Solution:
    def mySqrt(self, x: int) -> int:
        # Using Binary Search
        if x<=1:
            return x

        left = 1
        right = x//2
        while left<=right:
            mid = (right+left)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                right = mid-1
            else:
                left = mid+1
        return right