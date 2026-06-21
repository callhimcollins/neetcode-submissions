class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = {}
        for num in nums:
            if num in dictt:
                dictt[num] += 1
            else:
                dictt[num] = 1
        
        heap = []
        for key, value in dictt.items():
            heapValue = (value, key)
            if len(heap) < k:
                heapq.heappush(heap, heapValue)
            else:
                heapq.heappushpop(heap, heapValue)
        
        return [key for value, key in heap]