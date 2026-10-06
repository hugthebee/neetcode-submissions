class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for index, t in enumerate(temperatures):
            if index == 0: 
                stack.append(index)
                continue
            
            if temperatures[index-1] < t:
                while len(stack) != 0 and temperatures[stack[-1]] < t:
                    a = stack.pop()
                    ans[a] = index - a

            
            stack.append(index) 
        
        return ans


        