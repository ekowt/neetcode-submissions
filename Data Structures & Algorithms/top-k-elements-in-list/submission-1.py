class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        

        for i in counter:
            heapq.heappush(heap,(counter[i],i))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        res = [0]*(len(heap))
        for i in range(len(heap)):
            res[i] = heap[i][1]
        
        return(res)
        
        