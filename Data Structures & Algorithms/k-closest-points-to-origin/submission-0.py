class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return x ** 2 + y ** 2
        
        min_heap = []
        for x, y in points:
            pointValue = -(dist(x, y))
            distance = (pointValue, x, y)
            if len(min_heap) < k:
                heapq.heappush(min_heap, distance)
            else:
                heapq.heappushpop(min_heap, distance)
        
        return [[x,y] for pointValue, x, y in min_heap]