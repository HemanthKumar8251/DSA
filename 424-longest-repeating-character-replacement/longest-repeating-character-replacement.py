class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        window_size = 0
        max_freq = 0
        res = 0
        for right in range(len(s)):
            window_size += 1
            freq[s[right]]=freq.get(s[right],0)+1
            max_freq = max(freq.values())
            if window_size - max_freq > k:
                freq[s[left]]-=1
                left += 1
                window_size -= 1
            res = max(window_size,res)

        return res