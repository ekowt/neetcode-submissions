class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        visit = set()
        length = 0
        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l])
                l+=1
            
            visit.add(s[r])
            length = max(length,len(visit))
            
            
           
        
        return length