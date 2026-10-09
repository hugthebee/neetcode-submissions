class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        size = len(nums)
        j = size - 1 

        while i<=j:
            index = i + (j-i)//2
            
            if nums[index] > target:
                # print(1)
                j = index - 1

            elif nums[index] < target:
                # print(2)
                i = index + 1
            
            else:
                return index
        
        return -1