class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = [-1,-1]
        i,j = 0,len(numbers)-1

        while i<j:
            if numbers[i]+numbers[j] < target:
                i += 1
            elif numbers[i]+numbers[j] > target:
                j -= 1
            else:
                res = [i+1,j+1]
                break
        return res