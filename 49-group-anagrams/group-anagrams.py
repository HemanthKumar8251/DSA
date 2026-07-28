from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        # O(n*klogk) as we are using sorting
        # for i in strs:
        #     hash_map[''.join(sorted(i))].append(i)
        # return list(hash_map.values())

        # O(n*k) as we are using a count list
        for s in strs:
            count = [0]*26
            for i in s:
                count[ord(i)-ord('a')]+=1
            hash_map[tuple(count)].append(s)
        return list(hash_map.values())