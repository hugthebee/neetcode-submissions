class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = defaultdict(int)
        explored = set()

        for n in nums:
            seq[n] = 1
        
        ans = 0
        for key in seq:
            if key in explored:
                continue
            
            temp = key
            length = 1
            while (temp + 1) in seq:
                length+=1
                explored.add(temp + 1)
                temp+=1
            
            ans = max(ans, length)
        
        return ans