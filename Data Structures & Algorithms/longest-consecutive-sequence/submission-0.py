class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        
        visited = set()
        for num in nums:
            if num in visited:
                continue
            
            queue = deque([num])
            length = 0
            while queue:
                cur = queue.popleft()
                if cur in visited:
                    continue
                
                visited.add(cur)
                length += 1
                if cur - 1 in nums:
                    queue.append(cur - 1)
                
                if cur + 1 in nums:
                    queue.append(cur + 1)
            
            ans = max(ans, length)

        
        return ans


            
