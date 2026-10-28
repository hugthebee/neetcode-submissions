class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(lambda: defaultdict(dict))

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        i = timestamp

        while i>=0:
            if i in self.timeMap[key]:
                return self.timeMap[key][i]
            i-=1
        return ""
