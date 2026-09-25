class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = nums[0]
        seen = {}

        for i, n in enumerate(nums):
            seen[n] = i

        for i, num in enumerate(nums):
            if target - num in seen and seen[target-num]!=i:
                return [i, seen[target - num]]

        return []

