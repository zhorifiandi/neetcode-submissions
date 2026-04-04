from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        top_k_heap = []
        for num in counter:
            heappush(top_k_heap, (counter[num], num))
            if len(top_k_heap) > k:
                heappop(top_k_heap)

        return [num for _, num in top_k_heap]