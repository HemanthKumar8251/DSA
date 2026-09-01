class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            bit_sum = 0
            for num in nums:
                bit_sum += num>>i&1
            bit_sum %= 3
            res |= bit_sum<<i
        if res >= 2**31:
            res -= 2**32
        return res