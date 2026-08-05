class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""
        for i in range(n):
            left, right = i, i
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    if len(s[left:right+1]) > len(ans):
                        ans = s[left:right+1]
                    
                    left -= 1
                    right += 1
                else:
                    break
            
            left, right = i, i+1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    if len(s[left:right+1]) > len(ans):
                        ans = s[left:right+1]
                    
                    left -= 1
                    right += 1
                else:
                    break
        
        return ans