class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def explore(stack):
            visited = set()
            while stack:
                i, j = stack.pop()
                visited.add((i,j))

                for di, dj in directions:
                    new_i, new_j = i + di, j + dj
                    inRange = 0 <= new_i < m and 0 <= new_j < n
                    if inRange and (new_i, new_j) not in visited and heights[new_i][new_j] >= heights[i][j]:
                        stack.append((new_i, new_j))


            return visited

        # pacific ocean
        pacifics = []
        for j in range(n):
            pacifics.append((0,j))
        for i in range(m):
            pacifics.append((i,0))

        pacific_reachable = explore(pacifics)
        
        # atlantic ocean
        atlantics = []
        for j in range(n):
            atlantics.append((m-1,j))
        for i in range(m):
            atlantics.append((i,n-1))
        
        atlantic_reachable = explore(atlantics)
        
        return list(pacific_reachable.intersection(atlantic_reachable))