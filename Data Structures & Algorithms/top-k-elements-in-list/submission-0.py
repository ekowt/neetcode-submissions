class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        res = []

        for num in counter:
            heapq.heappush(heap,(counter[num],num))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        for i in range(k):
            res.append(heap[i][1])
        
        return(res)
