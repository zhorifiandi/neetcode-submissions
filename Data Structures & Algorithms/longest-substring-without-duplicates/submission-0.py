class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left, right = 0, 0
        curLen = 0
        lookup = set()

        while left < len(s) and right < len(s):
            while right < len(s) and s[right] not in lookup:
                lookup.add(s[right])
                right += 1
                curLen += 1
            
            lookup.remove(s[left])
            maxLength = max(maxLength, curLen)
            left += 1
            curLen -= 1
        

        return maxLength
