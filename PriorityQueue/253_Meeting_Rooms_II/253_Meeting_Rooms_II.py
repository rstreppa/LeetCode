import heapq

def minMeetingRooms(intervals):
  '''
    253	Meeting Rooms II
    Medium
    Problem Statement
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

    For example, given [[0, 30],[5, 10],[15, 20]], return 2.
  '''

    # 1. Sorting: First, sort the meeting intervals by their start times. This will allow you to handle the meetings in the order they occur.
    # 2. Priority Queue (Min-Heap): Initialize a min-heap to keep track of meeting end times. The reason for using a min-heap is that it allows you to efficiently find the earliest ending meeting among the currently ongoing meetings.
    # 3. Iterate Through Meetings: Loop through the sorted meetings. For each meeting, check the min-heap to see if any ongoing meeting ends before or at the same time this meeting starts. If so, you can use the same room for this meeting, and you need to update the end time in the min-heap.
    # 4. Count Rooms: The size of the heap will give you the minimum number of rooms needed at any point in time, because the heap contains end times for all ongoing meetings.
  
  if not intervals:
      return 0
    
  # Initialize a heap
  free_rooms = []
    
  # Sort the meetings in increasing order of their start time.
  intervals.sort(key=lambda x: x[0])
    
  # Add the first meeting. We have to give a new room to the first meeting.
  heapq.heappush(free_rooms, intervals[0][1])
    
  # For all the remaining meeting rooms
  for i in intervals[1:]:
        
      # If the room due to free up the earliest is free, assign that room to this meeting.
      if free_rooms[0] <= i[0]:
          heapq.heappop(free_rooms)
        
      # If a new room is to be assigned, then also we add to the heap.
      # If an old room is allocated, then also we have to add to the heap with updated end time.
      heapq.heappush(free_rooms, i[1])
        
  # The size of the heap tells us the minimum rooms required for all the meetings.
  return len(free_rooms)
