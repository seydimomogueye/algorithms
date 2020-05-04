class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f"[{self.start}, {self.end}]"


def merge_intervals(intervals):
    """
    Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
    """
    mergedIntervals = []
    intervals.sort(key=lambda x: x.start)
    
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
        interval = intervals[i]

        if interval.start <= end:
            end = max(end, interval.end)
        else:
            mergedIntervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    mergedIntervals.append(Interval(start, end))
    return mergedIntervals


def insert_interval(instervals, new_interval):
    mergedInterval = []
    for i in range(len(intervals) - 1):
        interval = intervals[i]
        if interval[1] < s

    return mergedIntervals

print(insert_interval([[1,3], [5,7], [8,12]], [4, 6]))
print(insert_interval([[1,3], [5,7], [8,12]], [4, 10]))
print(insert_interval([[2,3],[5,7]], [1, 4]))

