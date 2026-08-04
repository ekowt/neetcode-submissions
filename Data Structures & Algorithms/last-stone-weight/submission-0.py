class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        heap = []

        for i in stones:
            heapq.heappush(heap,-i)
        
        while len(heap) > 1:
            x = -heapq.heappop(heap)  # largest
            y = -heapq.heappop(heap)  # second largest


            if x != y:
                heapq.heappush(heap, -(x - y))
        return -heap[0] if heap else 0