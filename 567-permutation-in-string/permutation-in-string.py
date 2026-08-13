class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = Counter(s1)
        freq_window = Counter()
        left = 0
        for right in range(len(s2)):
            freq_window[s2[right]] = freq_window.get(s2[right],0)+1
            if right-left+1>len(s1):
                freq_window[s2[left]]-=1
                left +=1
            if freq_s1 & freq_window == freq_s1:
                return True
        return False