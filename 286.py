# Walls and Gates

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n, m = len(rooms), len(rooms[0])
        visited = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque([]) # store as (i,j) pair

        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue.append((i,j))

        while queue:
            i, j = queue.popleft()
            visited.add((i,j))

            for di, dj in directions:
                ni, nj = i+di, j+dj
                # collision check
                if not (0 <= ni < n and 0 <= nj < m):
                    continue
                # get shortest distance and queue neighbors 
                if ((ni, nj)) not in visited and rooms[ni][nj] == 2147483647:
                    rooms[ni][nj] = rooms[i][j] + 1
                    queue.append((ni,nj))
                  
