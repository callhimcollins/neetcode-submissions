class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = [0] * 26
        t_dict = [0] * 26
        for char in s:
            s_dict[ord(char) - ord('a')] += 1
        
        for char in t:
            t_dict[ord(char) - ord('a')] += 1
        
        return s_dict == t_dict