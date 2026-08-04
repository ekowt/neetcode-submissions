class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word = ''
        res = defaultdict(list)
        for i in strs:
            word = ''.join(sorted(i))
            res[word].append(i)
        return(list(res.values()))