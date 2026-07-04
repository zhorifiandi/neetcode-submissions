class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = dict()

        # convert t to t_counter
        # to do
        for k in t:
            if k not in t_counter:
                t_counter[k] = 0
            t_counter[k] += 1

        def contains(s_counter, t_counter):
            for k in t_counter:
                if k not in s_counter:
                    return False
                
                if t_counter[k] > s_counter[k]:
                    return False
            
            return True

        for size in range(len(t), len(s) + 1):
            left = 0
            right = 0
            
            s_counter = dict()
            while left + size <= len(s):
                if s[right] not in s_counter:
                    s_counter[s[right]] = 0
                s_counter[s[right]] += 1
                right += 1

                if right - left < size:    
                    continue
                
                if contains(s_counter, t_counter):
                    return s[left:right]
                
                s_counter[s[left]] -= 1
                if s_counter[s[left]] == 0:
                    del s_counter[s[left]]
                left += 1
        
        return ""
                    



