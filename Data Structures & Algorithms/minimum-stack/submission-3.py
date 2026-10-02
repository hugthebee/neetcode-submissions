class MinStack:

    def __init__(self):
        self.main = []
        self.helping = []

    def push(self, val: int) -> None:
        if len(self.helping) == 0:
            self.main.append(val)
            self.helping.append(val)
            return 
        
        currMin = self.helping[-1]

        if currMin > val:
            self.main.append(val)
            self.helping.append(val)
        else: 
            self.main.append(val)
            self.helping.append(currMin)

    def pop(self) -> None:
        self.main.pop()
        self.helping.pop()

    def top(self) -> int:
        return self.main[-1]
        

    def getMin(self) -> int:
        return self.helping[-1]
        
