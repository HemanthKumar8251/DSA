class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        res = 0
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            max_freq = max(freq.values())
            window_size = right-left+1
            if window_size - max_freq > k:
                freq[s[left]]-=1
                left += 1
            res = max(right-left+1,res)

        return res