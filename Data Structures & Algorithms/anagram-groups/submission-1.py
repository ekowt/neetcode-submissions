class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        word =""
        for c in strs:
            word = ''.join(sorted(c))
            res[word].append(c)
        return(list(res.values()))