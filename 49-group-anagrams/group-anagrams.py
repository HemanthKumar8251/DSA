from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for i in strs:
            hash_map[''.join(sorted(i))].append(i)
        return list(hash_map.values())