class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap  = []*len(nums)
        res = []

        for i in counter:
            heapq.heappush(heap,(counter[i],i))
        

        while len(heap) > k:
            heapq.heappop(heap)
        
        for i in range(len(heap)):
            res.append(heap[i][1])
        
        return(res)