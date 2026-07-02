class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            |AAABA|BB -> counter {A:4, B:1} -> windowSize - counter[ch] <= k  -> true
        """

        ans = 0
        left = right = 0
        counter = dict()

        def possible(windowSize, counter):
            for c in counter:
                if windowSize - counter[c] <= k:
                    return True
            
            return False


        while left < len(s):
            while right < len(s):
                if s[right] not in counter:
                    counter[s[right]] = 0
                
                
                windowSize = right - left + 1

                counter[s[right]] += 1
                if not possible(windowSize, counter):
                    counter[s[right]] -= 1
                    break
                
                ans = max(ans, windowSize)
                right += 1
            
            counter[s[left]] -= 1
            left += 1
        
        return ans

                