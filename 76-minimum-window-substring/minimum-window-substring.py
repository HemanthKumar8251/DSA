class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_start = -1
        min_len = inf
        t_freq = Counter(t)
        left = 0
        cur_freq = Counter()
        target_char_count = 0
        for right,ch in enumerate(s):
            cur_freq[ch] += 1
            if ch in t_freq and cur_freq[ch]<=t_freq[ch]:
                target_char_count += 1
            while target_char_count == len(t):
                cur_length = right-left+1
                if cur_length<min_len:
                    min_start = left
                    min_len = cur_length
                left_ch = s[left]
                if cur_freq[left_ch]<=t_freq[left_ch]:
                    target_char_count -= 1
                cur_freq[left_ch] -= 1
                left += 1

        return "" if min_start==-1 else s[min_start:min_start+min_len]