class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        s1_counter = dict()
        for c in s1:
            if c not in s1_counter:
                s1_counter[c] = 0
            s1_counter[c] += 1

        s2_counter = dict()
        # for i in range(m):
        #     if s2[i] not in s2_counter:
        #         s2_counter[s2[i]] = 0
        #     s2_counter[s2[i]] += 1
        
        def included(c1, c2):
            for k in c2:
                if k not in c1 or c1[k] != c2[k]:
                    return False
            
            return True
        
        left = 0
        right = 0
        while right < n:
            if s2[right] not in s2_counter:
                s2_counter[s2[right]] = 0
            s2_counter[s2[right]] += 1
            right += 1

            if right - left < m:
                continue 

            # print(s1_counter, s2_counter)
            if included(s1_counter, s2_counter):
                return True
            
            s2_counter[s2[left]] -= 1
            if s2_counter[s2[left]] == 0:
                del s2_counter[s2[left]]

            left += 1
        
        return False

