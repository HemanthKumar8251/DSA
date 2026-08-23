class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Using 2 Binary Searches one for Row and one for Col
        m, n = len(matrix), len(matrix[0])
        # 1. Binary search to find the correct row
        mlow, mhigh = 0, m - 1
        target_row = -1
        
        while mlow <= mhigh:
            mid = (mlow + mhigh) // 2
            # Check if target falls within the boundary of the current row
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                target_row = mid
                break
            elif target < matrix[mid][0]:
                mhigh = mid - 1
            else:
                mlow = mid + 1
                
        # If target_row is still -1, the target is out of the matrix overall bounds
        if target_row == -1:
            return False
            
        # 2. Binary search within the identified row
        nlow, nhigh = 0, n - 1
        while nlow <= nhigh:
            mid = (nlow + nhigh) // 2
            if matrix[target_row][mid] == target:
                return True
            elif target < matrix[target_row][mid]:
                nhigh = mid - 1
            else:
                nlow = mid + 1 
        return False