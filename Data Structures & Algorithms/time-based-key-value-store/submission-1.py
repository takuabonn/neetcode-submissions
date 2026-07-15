class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        print(self.hashMap)
        if key not in self.hashMap:
            return ""
        
        tList = self.hashMap[key]

        l, r = 0, len(tList)-1
        result = -1
        while l <= r:
            mid = l + (r-l)//2
            pt, v = tList[mid]
            if pt <= timestamp:
                result = v
                l = mid + 1
            else:
                r = mid - 1
            if l > r:
                if result == -1:
                    return ""
                return result
        
