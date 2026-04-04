class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = {}
        t_counter = {}
        for c in s:
            if c not in s_counter:
                s_counter[c] = 0
            
            s_counter[c] += 1
        
        for c in t:
            if c not in t_counter:
                t_counter[c] = 0
            
            t_counter[c] += 1

        for c in s_counter:
            if c not in t_counter:
                return False
            
            if s_counter[c] != t_counter[c]:
                return False
            
        
        return len(s_counter) == len(t_counter)