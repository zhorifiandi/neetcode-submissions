from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [s*-1 for s in stones]
        heapify(stones)

        while len(stones) > 1:
            y = heappop(stones)
            y *= -1
            x = heappop(stones)
            x *= -1

            if x < y:
                heappush(stones, -1*(y-x))
        
        if len(stones) == 0:
            return 0
        
        return -1 * stones[0]
