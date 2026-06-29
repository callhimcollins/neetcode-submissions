class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        sett = set()
        max_len = 0
        l = 0

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            max_len = max(max_len, r- l + 1)
        
        return max_len