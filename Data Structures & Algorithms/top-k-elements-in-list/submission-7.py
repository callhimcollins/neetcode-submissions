from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_dict = Counter(nums)
        res = []

        for key, value in f_dict.items():
            if len(res) < k:
                heapq.heappush(res, (value, key))
            else:
                heapq.heappushpop(res, (value, key))
        
        return [num for freq, num in res]