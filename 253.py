# Meeting Rooms II

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort(key=lambda x: x[0])
        output = 0
        curr = 0

        for interval in intervals:
            # free up all available rooms
            if len(heap) and heap[0] <= interval[0]:
                heapq.heappop(heap)
                curr -= 1

            # take up room
            curr += 1
            output = max(curr, output)
            heapq.heappush(heap, interval[1])

        return output
