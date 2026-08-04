class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        visit = {}
        res = []
        res1=[]

        for i in nums:
            if i in visit:
                visit[i]+=1
            else:
                visit[i] = 1

        for key,val in visit.items():
            heapq.heappush(heap,[-val,key])
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return(res)
        
        



