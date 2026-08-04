class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)

        bucket = [[] for _ in range(len(nums)+1)]

        for nums, count in freq.items():
            bucket[count].append(nums)
        
        res = []
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res)==k:
                    return res
