class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for w in s:
            freq1[ord(w) - ord('a')]+=1

        for w in t:
            freq2[ord(w) - ord('a')]+=1

        return freq1 == freq2

        
        