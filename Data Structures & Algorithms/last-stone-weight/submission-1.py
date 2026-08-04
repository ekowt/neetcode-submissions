class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        sort = stones
        while  len(sort)> 1:
            sort = sorted(sort)
            print(sort)
            y = sort.pop()
            x = sort.pop()
            print(x,y)
            if x < y:
                sort.append(y-x)
       
        return sort[0] if sort else 0
       
            