class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

         
        l=0
        visit = set()
        length = 0
        for r in range(len(s)):
            while s[r] in visit:
                length = max(length, len(visit))
                visit.remove(s[l])
                l+=1
            
            visit.add(s[r])
            length = max(length, len(visit))
        return length


        


        """
        input = string
        output = int
        goal is to return the longest substring without duplicates


        Algorithm: Two Pointers
        one pointer starts at 0 while the other keeps expanding the window until if finds an element that is in the set. Once found we shift the left pointer and keep expanding the window then repeat the process again. also taking account off the greatest length at each window

        approach
        set l to 0
        loop through the string and expanding the window. 
        add each element to the set
        if a duplicate is found take the length of the current window
        remove s[l] from the set
        repeat the process
        return the length
        """