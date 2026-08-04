class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        
        height = 0
        for i  in range(len(heights)):
            for j in range(1,len(heights)):
                height = min(heights[i],heights[j])
                length = height*(j-i)
                area = max(area,length)
       
        return(area)