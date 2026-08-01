class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board == "":
            return True

        m, n = len(board), len(board[0])
        def foundWord(i, j, path):
            wordIndex = len(path)
            if wordIndex == len(word):
                return True

            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                if not (0 <= i + di < m and 0 <= j + dj < n):
                    continue
                
                if (i+di, j+dj) in path:
                    continue
                
                if board[i+di][j+dj] == word[wordIndex]:
                    if foundWord(i+di, j+dj, path.union(set([(i+di, j+dj)]))):
                        return True
            
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and foundWord(i, j, set([(i,j)])):
                    return True
        

        return False