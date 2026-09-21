class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""

        for s in strs:
            l = len(s)
            ans += str(l)
            ans += "*"
            ans += s

        return ans


    def decode(self, s: str) -> List[str]:
        l = len(s)
        size = ""
        ans = []
        i=0

        while i<l:
            size = ""

            while s[i] != "*":
                size += s[i]
                i+=1
            i+=1
            length = int(size)
            ans.append(s[i:i+length])
            i+=length

        return ans
        
