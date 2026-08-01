from heapq import heappush, heappop

def maxHeappush(heap, num):
    heappush(heap, -num)

def maxHeappop(heap):
    num = heappop(heap)
    return -num

def maxPeek(heap):
    return -heap[0]

class MedianFinder:

    def __init__(self):
        # maxHeap
        self.leftHeap = []
        # minHeap
        self.rightHeap = []

    def addNum(self, num: int) -> None:
        # insert
        if len(self.leftHeap) == 0:
            maxHeappush(self.leftHeap, num)
        elif num <= maxPeek(self.leftHeap):
            maxHeappush(self.leftHeap, num)
        else:
            heappush(self.rightHeap, num)
        
        # rebalance
        if len(self.leftHeap) - len(self.rightHeap) > 1:
            movedNum = maxHeappop(self.leftHeap)
            heappush(self.rightHeap, movedNum)
        elif len(self.rightHeap) > len(self.leftHeap):
            movedNum = heappop(self.rightHeap)
            maxHeappush(self.leftHeap, movedNum)

    def findMedian(self) -> float:
        size = len(self.leftHeap) + len(self.rightHeap)
        if size % 2 == 1:
            return maxPeek(self.leftHeap)
        
        return (maxPeek(self.leftHeap) + self.rightHeap[0]) / 2
        