class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        counter,window = {},{}
        counter = Counter(t)
        res,resLen = [-1,-1],sys.maxsize
        have, need = 0, len(counter)
        l=0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1+window.get(c,0)
            if c in counter and window[c] == counter[c]:
                have+=1
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]]-=1
                if s[l] in counter and window[s[l]] < counter[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != sys.maxsize else ""