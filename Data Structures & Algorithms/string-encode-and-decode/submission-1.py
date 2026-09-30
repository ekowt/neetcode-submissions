class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for s in strs:
            word += str(len(s)) +'#' + s
        return (word)

    def decode(self, s: str) -> List[str]:
        res = []
        length = 0
        word = ''
        i = 0
        j = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            word = s[i:j]
            res.append(word)
            i=j
        return (res)
      