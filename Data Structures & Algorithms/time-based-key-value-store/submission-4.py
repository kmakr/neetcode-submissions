class TimeMap:

    def __init__(self):
        self.history = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.history[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # find target by target as timestamp
        target = timestamp

        l = 0
        r = len(self.history[key]) - 1
        res = ""

        while (l <= r) :

            mid = (l + r) // 2

            if (target >= self.history[key][mid][1]):
                l = mid + 1
                res = self.history[key][mid][0]
            
            else:
                r = mid - 1
            
           
        return res
