class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row_idx: (set)
        lookup_row = defaultdict(set)
        # col_idx: (set)
        lookup_col = defaultdict(set)
        # group_idx: (set)
        # i < 3 and j < 3: group_idx = 0
        # i < 3 and 3 <= j < 6: group_idx = 1
        # .....
        lookup_group = defaultdict(set)


        # Populate lookup dictionaries
        # TODO

        for i in range(len(board)):
            for j in range(len(board[i])):
                cur = board[i][j]
                if cur == ".":
                    continue
                
                if cur in lookup_row[i] or cur in lookup_col[j] or cur in lookup_group[(i//3,j//3)]:
                    return False
                
                lookup_row[i].add(cur)
                lookup_col[j].add(cur)
                lookup_group[(i//3,j//3)].add(cur)
        
        return True


