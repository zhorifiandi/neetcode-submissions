class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = list(s)
            key.sort()
            groups["".join(key)].append(s)
        
        ans = []
        for key in groups:
            ans.append(groups[key])
        
        return ans
