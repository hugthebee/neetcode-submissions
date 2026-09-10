class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for s in strs:
            word = "".join(sorted(s))

            if word in freq:
                freq[word].append(s)
            else:
                freq[word] = [s]

        return list(freq.values())