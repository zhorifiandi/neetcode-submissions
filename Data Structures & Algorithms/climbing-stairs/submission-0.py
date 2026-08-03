class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:
        # climbStairs(0) = 1
        # climbStairs(1) = 1
        # climbStairs(2) = (take 2 step) climbStairs(0) + (take 1 step) climbStairs(1)
        # climbStairs(3) = (take 2 step) climbStairs(1) + (take 1 step) climbStairs(2)

        if n <= 1:
            return 1
        
        if n in self.cache:
            return self.cache[n]

        ans = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cache[n] = ans
        return ans