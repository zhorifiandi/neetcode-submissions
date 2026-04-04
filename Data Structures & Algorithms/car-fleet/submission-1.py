class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [[1], [2], [], [], [2], [], [], [1], [], []]
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort(reverse=True)
        
        # print(cars)

        stack = []
        for i in range(n):
            s = cars[i][1]
            time_to_reach_end = (target - cars[i][0]) / s
            while stack and time_to_reach_end <= stack[-1][0]:
                time_to_reach_end, s = stack.pop()
            
            stack.append((time_to_reach_end, s))
            # print(stack)

        return len(stack)
