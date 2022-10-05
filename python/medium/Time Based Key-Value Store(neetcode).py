class TimeMap:
    def __init__(self):
        self.time_map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value = self.time_map.get(key, [])
        res = ''
        l, r = 0, len(value) - 1
        while l <= r:
            m = (l + r) // 2
            if value[m][1] > timestamp:
                r = m - 1
            elif value[m][1] < timestamp:
                res = value[m][0]
                l = m + 1
            else:
                res = value[m][0]
                break

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)