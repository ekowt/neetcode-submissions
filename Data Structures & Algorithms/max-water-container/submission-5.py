class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area = 0
        l = 0
        r = len(heights)-1

        while l<r:
            length = r-l
            height = min(heights[l],heights[r])
            area = max(area,length*height)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return(area)




        """
        input : array
        output: int
        goal: return the greatest area

        constraints
        -can the array have length of 1
        - can the array have negatives
        - is the answer unique

        approach
        Two pointers
        have l start at 0 r at the end
        length = r-l
        height = min(heights[l],heights[r])
        area = max(area,length*heights)
        if nums[l] < nums[r]:
            l+=1
        """
     