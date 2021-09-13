# 794. Valid Tic-Tac-Toe State
# https://leetcode.com/problems/valid-tic-tac-toe-state/

["XOX",
 "OOX",
 "XO "]


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xcount = 0
        ocount = 0
        for row in board:
            for ch in row:
                if ch == 'X':
                    xcount += 1
                elif ch == 'O':
                    ocount += 1

        print(xcount, ocount)
        if not (xcount == ocount or xcount == ocount + 1):
            return False

        xwins = 0
        owins = 0
        for row in board:
            if row == "XXX":
                xwins += 1
            elif row == "OOO":
                owins += 1
        for i in range(0, 3):
            col = board[0][i] + board[1][i] + board[2][i]
            if col == "XXX":
                xwins += 1
            elif col == "OOO":
                owins += 1

        diag1 = board[0][0] + board[1][1] + board[2][2]
        diag2 = board[2][0] + board[1][1] + board[0][2]
        for diag in [diag1, diag2]:
            if diag == "XXX":
                xwins += 1
            elif diag == "OOO":
                owins += 1

        if xwins > 0 and owins > 0:
            return False
        if xwins > 1 and xcount != 5:
            return False
        if owins > 1 and ocount != 5:
            return False
        if xwins > 0 and xcount != ocount + 1:
            return False
        if owins > 0 and xcount != ocount:
            return False
        return True