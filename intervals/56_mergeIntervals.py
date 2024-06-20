'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEle = output[-1][1]
            if lastEle >= start:
                output[-1][1] = max(lastEle, end)
            else:
                output.append([start, end])

        return output
'''
Time Complexity: O(nlogn) where n is the number of intervals
Space Complexity: O(n)
**********************
Summary Statistics:
Runtime: 108 ms, faster than 98.52% of Python3 online submissions for Merge Intervals.
Memory Usage: 21 MB, less than 32.42% of Python3 online submissions for Merge Intervals.
'''
