# Meeting Rooms II

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(heap, intervals[0][1])
        output = 1
        curr = 1

        for interval in intervals[1:]:
            # free up all available rooms
            if len(heap) and heap[0] <= interval[0]:
                heapq.heappop(heap)
                curr -= 1

            # take up room
            curr += 1
            output = max(curr, output)
            heapq.heappush(heap, interval[1])

        return output
