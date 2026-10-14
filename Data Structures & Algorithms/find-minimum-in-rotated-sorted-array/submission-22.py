class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        size = len(nums)
        e = size - 1

        if nums[0] < nums[e]:
            return nums[0]
        # if we find the rotated point we can easily find min element
        while s<e:
            mid = s + (e-s)//2 

            if nums[e] < nums[mid]:
                s = mid + 1
            
            else:
                e = mid

        return nums[s]









