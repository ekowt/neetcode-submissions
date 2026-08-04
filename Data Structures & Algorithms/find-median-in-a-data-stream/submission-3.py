class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large,-1*num)
        if self.large and self.small and  (-1*self.large[0] > self.small[0]):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)

        if len(self.large) > len(self.small) +1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*val)
        


    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return -1*self.large[0]
        elif len(self.small) > len(self.large):
            return (self.small[0])
     
    
        
        return ((self.small[0]) + -1*self.large[0])/2
        
        