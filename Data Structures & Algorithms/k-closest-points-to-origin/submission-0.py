from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # element of the heap (distance, i)
        heap = []

        for i in range(len(points)):
            x, y = points[i]
            distance = math.sqrt(x**2 + y ** 2)
            heappush(heap, (distance, i))
        
        ans = []
        for _ in range(k):
            distance, i = heappop(heap)
            ans.append(points[i])

        return ans