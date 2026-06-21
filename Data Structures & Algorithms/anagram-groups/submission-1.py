class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            strkey = [0] * 26
            for char in word:
                strkey[ord(char) - ord('a')] += 1
            key = tuple(strkey)
            res[key].append(word)
            
        return list(res.values())