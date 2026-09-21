class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Using Floyd's cycle detection alogrithm
        # We need to Phase1 and Phase2 to get the duplicate value
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        slow = 0
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow