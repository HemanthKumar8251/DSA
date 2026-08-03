class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        flag = 0
        version1 = list(map(int,version1.split('.')))
        version2 = list(map(int,version2.split('.')))
        for s,j in zip_longest(version1,version2,fillvalue=0):
            if s==j:
                continue
            if s<j:
                return -1
            else:
                return 1
        return 0