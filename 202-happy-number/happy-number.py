class Solution:
    def isHappy(self, n: int) -> bool:
        def digitSquareSum(num):
            return sum(int(d)**2 for d in str(num))
        slow,fast = n,digitSquareSum(n)
        while fast!=1 and slow!=fast:
            slow = digitSquareSum(slow)
            fast = digitSquareSum(digitSquareSum(fast))
        return fast == 1