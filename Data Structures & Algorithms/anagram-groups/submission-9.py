class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word = ''
        mapper = defaultdict(list)
        for i in strs:
            word = ''.join(sorted(i))
            mapper[word].append(i)
        
        return(list(mapper.values()))
            
            