class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # # Using Math
        # n = len(nums)
        # missingNum = (n*(n+1)//2)-sum(nums)
        # return missingNum

        # # Logical way of using the index values
        # # Sum of the index values is the total sum - each element
        # # Gives the missing number 
        # res = len(nums)
        # for i,num in enumerate(nums):
        #     res += i-num
        # return res

        # Using bit Manipulation with similar logic as above
        # Using XOR we get a^b^b = a
        # res ^ i ^ num
        res = len(nums)
        for i,num in enumerate(nums):
            res = res^i^num
        return res