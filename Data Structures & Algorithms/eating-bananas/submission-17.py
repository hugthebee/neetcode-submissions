class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = max(piles)
        best = e
        while s<=e:
            mid = s + (e-s+1)//2
            hours = 0

            for p in piles:
                hours+=math.ceil(p/mid)

            if hours > h:
                # discard
                s = mid + 1
            
            elif hours <= h:
                best = min(best, mid)
                e = mid - 1
        
        return best
        