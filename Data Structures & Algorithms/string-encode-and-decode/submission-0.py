class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append("#")
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        # print(s)
        arr = []
        i = 0
        while i < len(s) and s[i] == "#":
            i += 1
            wordLenStr = ""
            while i < len(s) and s[i] != "#":
                wordLenStr += s[i]
                i += 1
            
            i += 1
            wordLen = int(wordLenStr)
            arr.append(s[i:i+wordLen])
            i += wordLen
        
        return arr


