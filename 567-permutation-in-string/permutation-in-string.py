class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ##Using Counter which gives a freq dict
        # freq_s1 = Counter(s1)
        # freq_window = Counter()
        # left = 0
        # for right in range(len(s2)):
        #     freq_window[s2[right]] = freq_window.get(s2[right],0)+1
        #     if right-left+1>len(s1):
        #         freq_window[s2[left]]-=1
        #         left +=1
        #     if right-left+1==len(s1) and freq_s1 & freq_window == freq_s1:
        #         return True
        # return False

        # Using a list of size 26 to hash characters with ord(char)-ord('a')
        if len(s1)>len(s2):
            return False
        
        s1_freq = [0]*26
        window_freq = [0]*26

        for char in s1:
            s1_freq[ord(char)-ord('a')]+=1

        for i in range(len(s1)):
            window_freq[ord(s2[i])-ord('a')]+=1

        if s1_freq == window_freq:
            return True

        for i in range(len(s1),len(s2)):
            window_freq[ord(s2[i])-ord('a')]+=1
            window_freq[ord(s2[i-len(s1)])-ord('a')]-=1
            if window_freq==s1_freq:
                return True

        return False