class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        heap = []
        res = []
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1
        

        for i,j in freq.items():
            heapq.heappush(heap,[-j,i])
        
        
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res
        
    