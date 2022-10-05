from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)
        return None

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))
        return None

    def get(self, key: str, timestamp: int) -> str:

        def binary_search():
            l, r = 0, len(self.time_map[key]) - 1
            while l <= r:
                m = (l + r) // 2
                if self.time_map[key][m][1] > timestamp:
                    r = m - 1
                elif self.time_map[key][m][1] < timestamp:
                    l = m + 1
                else:
                    break
            return m

        if self.time_map[key][0][1] > timestamp:
            return ''
        else:
            return self.time_map[key][binary_search()][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)