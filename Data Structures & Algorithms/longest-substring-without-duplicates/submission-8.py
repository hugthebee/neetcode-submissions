class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = 0
        i = 0
        j = len(s) - 1
        uniq = set()

        while (i + window) <= j:
            char = s[i+window]
            if char not in uniq:
                uniq.add(char)
                window+=1
            
            else:
                longest=max(longest, window)
                uniq.remove(s[i])
                i+=1
                window-=1
        
        longest=max(longest, window)
        return longest