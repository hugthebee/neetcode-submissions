class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        ans = []
        length = len(nums) - 1

        for index, num in enumerate(sort):
            if index > 0 and num == sort[index - 1]:
                continue

            target = -1 * num
            i = index + 1
            j = length

            while i<j:
                if sort[i] + sort[j] > target:
                    j-=1
                
                elif sort[i] + sort[j] < target:
                    i+=1
                
                else: 
                    ans.append([num, sort[i], sort[j]])
                    j-=1
                    i+=1

                    while i<j and sort[i] == sort[i-1]:
                        i+=1
                    while i<j and sort[j] == sort[j+1]:
                        j-=1
                    
        
        return ans