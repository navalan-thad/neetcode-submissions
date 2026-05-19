class TimeMap:

    def __init__(self):
        self.kv = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.kv:
            self.kv[key].append((value, timestamp))
        else:
            self.kv[key] = [(value, timestamp)]
        
    def get(self, key: str, timestamp: int) -> str:

        if key in self.kv:
            values = self.kv[key]
            L = 0
            R = len(values) - 1
            while L <= R:
                mid = (L + R) // 2
                if timestamp < values[mid][1]:
                    R = mid - 1
                elif timestamp > values[mid][1]:
                    L = mid + 1
                else:
                    return values[mid][0]
            return values[R][0] if R >= 0 else ""

        return ""
        
