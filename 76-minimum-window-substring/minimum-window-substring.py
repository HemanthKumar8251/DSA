class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        # Taking initial min_index and min_len
        min_start = -1
        min_len = inf

        # Frequencies of target string
        t_freq = Counter(t)

        # Initializing the left/start pointer to 0th index
        left = 0

        # Creating a new Counter object for keeping track of frequencies in s
        cur_freq = Counter()

        # Keeps track of the count of curr matched characters of t in s
        target_char_count = 0

        # Traverse s, using enumerate to easily access the character and index
        for right,ch in enumerate(s):
            cur_freq[ch] += 1 # Updating the frequencies of characters in s

            # Check if the frequency is valid and increment target_char_count
            if ch in t_freq and cur_freq[ch]<=t_freq[ch]:
                target_char_count += 1

            # Once the target is achieved we get the min_start,min_len
            # Then shrink the window from left until the target_char_count is effected i.e,
            # we have removed a required element and looking for min_len, min_start
            while target_char_count == len(t):
                cur_length = right-left+1

                # Check and update min_len,min_start
                if cur_length<min_len:
                    min_start = left
                    min_len = cur_length
                left_ch = s[left]
                # Update the target_char_count and frequncy of left ele in cur_freq 
                if cur_freq[left_ch]<=t_freq[left_ch]:
                    target_char_count -= 1
                cur_freq[left_ch] -= 1
                # Shrink the window
                left += 1

        # Check min_start and return result
        return "" if min_start==-1 else s[min_start:min_start+min_len]