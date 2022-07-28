class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda i : i[0])
        currEnd = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            if start < currEnd:
                res += 1
                currEnd = min(currEnd, end)
                
            else:
                currEnd = end


        return res