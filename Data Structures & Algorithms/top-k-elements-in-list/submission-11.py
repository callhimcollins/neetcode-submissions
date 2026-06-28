from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_dict = Counter(nums)
        n = len(nums)
        res = [0] * (n + 1)

        for value, freq in f_dict.items():
            if res[freq] == 0:
                res[freq] = [value]
            else:
                res[freq].append(value)
        
        ret = []
        for i in range((n), -1, -1):
            if res[i] != 0:
                ret.extend(res[i])
            else: continue

            if len(ret) == k:
                break
        
        return ret



