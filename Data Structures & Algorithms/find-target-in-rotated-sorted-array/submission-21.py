class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        size = len(nums)
        l = size - 1

        while s<=l:
            mid = s + (l-s+1)//2
            print(mid)

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[size - 1]:
                # pivot is to the right of mid

                if nums[mid] < target:
                    s = mid + 1
                
                elif nums[mid] > target and target > nums[size - 1]:
                    l = mid - 1
                
                else: 
                    s = mid + 1
            
            elif nums[mid] <= nums[size - 1]:
                # pivot is to the left of mid

                if nums[mid] > target:
                    l = mid - 1
                
                elif nums[mid] < target and target <= nums[size - 1]:
                    s = mid + 1
                
                else: 
                    l = mid - 1
            
        return -1
                
