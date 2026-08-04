class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        print(counter)
        print(counter.most_common(k))
        res = []
        for i in counter.most_common(k):
            res.append(i[0])
        return(res)
      
        #print(counter.most_common(k))