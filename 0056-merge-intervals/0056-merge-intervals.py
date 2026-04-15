class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:           # overlap → merge
                merged[-1][1] = max(last_end, end)
            else:                           # no overlap → new interval
                merged.append([start, end])

        return merged