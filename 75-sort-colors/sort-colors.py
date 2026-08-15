class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # Brute Force O(N+K) K-is higest value in nums here it's just 3
        # # Time and O(U) Space U-is the number of unique values here it's just 3
        # hash_map = defaultdict(int)
        # for num in nums:
        #     hash_map[num]+=1
        # j = 0
        # for i in range(len(nums)):
        #     while j not in hash_map:
        #         j+=1
        #     nums[i]=j
        #     hash_map[j]-=1
        #     if hash_map[j]==0:
        #         j+=1

        # Pointers Approch
        red=white=0
        blue = len(nums)-1
        while white<=blue:
            if nums[white]==0:
                nums[white],nums[red]=nums[red],nums[white]
                red += 1
                white += 1
            elif nums[white]==2:
                nums[white],nums[blue]=nums[blue],nums[white]
                blue-=1
            else:
                white+=1
                 