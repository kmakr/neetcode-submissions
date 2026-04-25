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

        while (l <= r) :

            mid = (l + r) // 2

            if (target > self.history[key][mid][1]):
                l = mid + 1
            
            elif (target < self.history[key][mid][1]):
                r = mid - 1
            
            else:
                return self.history[key][mid][0]
            
        
       
        if timestamp > 1:
            return self.get(key, timestamp - 1)
        else:
            return ""
        
