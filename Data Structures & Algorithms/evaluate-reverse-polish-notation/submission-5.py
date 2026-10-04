class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        ans = int(tokens[0])

        for t in tokens:
            if t in operations:
                a = stack.pop()
                b = stack.pop()

                if t == "+":
                    ans = a + b
                
                elif t == "-":
                    ans = b - a

                elif t == "/":
                    ans = b / a

                elif t == "*":
                    ans = a * b
                
                stack.append(int(ans))

            else:
                stack.append(int(t))

        return int(ans)