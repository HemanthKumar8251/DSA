class Solution:
    def countArrangement(self, n: int) -> int:
        def backTracking(idx,seen):
            if idx>n:
                return 1
            count = 0
            for i in range(1,n+1):
                if i not in seen and (i%idx==0 or idx%i==0):
                    seen.add(i)
                    count += backTracking(idx+1,seen)
                    seen.remove(i)
            return count
        seen = set()
        return backTracking(1,seen)