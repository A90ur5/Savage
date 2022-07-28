class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda i : i[0])
        currStart = intervals[0][0]
        currEnd = intervals[0][1]
        for start, end in intervals[1:]: 
            if end <= currEnd:
                continue
            elif start <= currEnd and end > currEnd:
                currEnd = end

            else:
                res.append([currStart, currEnd])
                currStart = start
                currEnd = end
                
        res.append([currStart, currEnd])
        return res