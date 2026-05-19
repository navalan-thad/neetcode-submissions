class TimeMap:

    def __init__(self):
        self.kv = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.kv:
            self.kv[key].append((value, timestamp))
        else:
            self.kv[key] = [(value, timestamp)]
        
    def get(self, key: str, timestamp: int) -> str:

        values = ""
        if key in self.kv:
            values = self.kv[key]
            values.sort(key=lambda x: x[1], reverse=True)
            for i in values:
                if i[1] <= timestamp:
                    return i[0]
            return ""

        return values
        
