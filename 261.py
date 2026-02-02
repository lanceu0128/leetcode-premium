# Graph Valid Tree

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set([0])
        queue = deque([(-1, 0)]) # (prev, curr)

        while queue:
            prev, node = queue.popleft()

            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                if neighbor in visited:
                    return False

                queue.append((node, neighbor))
                visited.add(neighbor)

        return n == len(visited)
        
