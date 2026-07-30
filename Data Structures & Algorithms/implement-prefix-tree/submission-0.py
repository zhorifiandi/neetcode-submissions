class PrefixTree:

    def __init__(self):
        self.trie = {}
        self.EXIST = -1

    def insert(self, word: str) -> None:
        curLevelTrie = self.trie
        for ch in word:
            if ch not in curLevelTrie:
                curLevelTrie[ch] = {}
            
            curLevelTrie = curLevelTrie[ch]
        
        curLevelTrie[self.EXIST] = True

    def search(self, word: str) -> bool:
        curLevelTrie = self.trie
        for ch in word:
            if ch not in curLevelTrie:
                return False
            
            curLevelTrie = curLevelTrie[ch]
        
        return self.EXIST in curLevelTrie

    def startsWith(self, prefix: str) -> bool:
        curLevelTrie = self.trie
        for ch in prefix:
            if ch not in curLevelTrie:
                return False
            
            curLevelTrie = curLevelTrie[ch]
        
        return True
        