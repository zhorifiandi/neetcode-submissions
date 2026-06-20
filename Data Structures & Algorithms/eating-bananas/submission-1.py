class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        k -> [1, max(piles)] 
        piles = [1,4,3,2], h = 9
        k -> [1, 4], times = 4 < h
        """
        
        ans = max(piles)
        k_left, k_right = 1, max(piles)
        a = 0
        while k_left < k_right:
            k = (k_left + k_right) // 2
            times = 0
            for p in piles:
                times += math.ceil(p / k)
            
            if times > h:
                k_left = k + 1
            else:
                ans = k
                k_right = k
            
        
        return ans