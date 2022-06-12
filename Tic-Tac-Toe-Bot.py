#!/usr/bin/python
import os
import string
import sys

alphabet_string = string.ascii_uppercase

class Game:

    def __init__(self,turn, board, rows,cols,game_win):
        self.turn = turn
        self.board = board
        self.rows = rows
        self.cols = cols
        self.game_win = game_win

    def say_turn(self):
        print ("It is %s's turn, make your move") % self.turn

    def say_status(self):
        if (self.game_status == 'Os'):
            print("Congratulations, Circles Win")
        elif (self.game_status == 'Xs'):
            print("Congratulations, Xs Win")
        else:
            print("Ongoing")
    def change_turn(self):
        if self.turn == 'O':
            self.turn = 'X'
            return self.turn
        else:
            self.turn = 'O'
            return self.turn
    def show_board(self):
        for j in range(self.cols): 
            if j == 0:
                print("   "),
                print("%d   " % (j + 1)),
            else:
                print("%d   " % (j + 1)),
        print("\n")
        for r,c in sorted(self.board): 
            if (c == 0):
                print ((alphabet_string[r])),
                print(" "),
                print ("%s   " % self.board[r,c]),
            elif c == self.cols - 1 and self.board[r,c] == '_':
                print ("%s   " % self.board[r,c]),
                print ("\n")
            elif c == self.cols - 1:
                print ("%s   " % self.board[r,c]),
                print ("\n")
            else:
                print ("%s   " % self.board[r,c]),

    def check_rows(self):
        x_count = 0
        o_count = 0
        for r in range(self.rows):
            o_count = 0
            x_count = 0
            for c in range(self.cols):
                if self.board[r,c] == 'X'  and c <= self.cols - 1:
                    x_count += 1
                    o_count = 0
                    if x_count >= self.game_win: 
                        return 'Xs'
                elif self.board[r,c] == 'O'  and c <= self.cols - 1:
                    o_count += 1
                    x_count = 0
                    if o_count >= self.game_win: 
                        return 'Os'
                else:
                    o_count = 0
                    x_count = 0
        return 'Ongoing'

    def check_cols(self):
        x_count = 0
        o_count = 0
        for c in range(self.rows):
            o_count = 0
            x_count = 0
            for r in range(self.cols):
                if self.board[r,c] == 'X'  and r <= self.rows - 1:
                    x_count += 1
                    o_count = 0
                    if x_count >= self.game_win: 
                        return 'Xs'
                elif self.board[r,c] == 'O'  and r <= self.rows - 1:
                    o_count += 1
                    x_count = 0
                    if o_count >= self.game_win: 
                        return 'Os'
                else:
                    o_count = 0
                    x_count = 0
        return 'Ongoing'

    def check_diag_rupper(self):
        x_count = 0
        o_count = 0
        for r in range(self.rows):
            i = r
            o_count = 0
            x_count = 0
            #print(i)
            for c in range(self.cols - r):
                #print ("coord: %d,%d" % (i,c))
                if self.board[i,c] == 'X'  and r <= self.rows - 1 and c <= self.cols - 1:
                    i += 1
                    x_count += 1
                    o_count = 0
                    if x_count >= self.game_win: 
                        return 'Xs'
                elif self.board[i,c] == 'O'  and r <= self.rows - 1 and c <= self.cols - 1:
                    i += 1
                    o_count += 1
                    x_count = 0
                    if o_count >= self.game_win: 
                        return 'Os'
                else:
                    i += 1
                    o_count = 0
                    x_count = 0
        return 'Ongoing'

    def check_diag_rower(self):
        x_count = 0
        o_count = 0
        for c in range(1,self.cols):
            i = c
            o_count = 0
            x_count = 0
            for r in range(self.rows - c):
                if self.board[r,i] == 'X'  and r <= self.rows - 1 and c <= self.cols - 1:
                    i += 1
                    x_count += 1
                    o_count = 0
                    if x_count >= self.game_win: 
                        return 'Xs'
                elif self.board[r,i] == 'O'  and r <= self.rows - 1 and c <= self.cols - 1:
                    i += 1
                    o_count += 1
                    x_count = 0
                    if o_count >= self.game_win: 
                        return 'Os'
                elif self.board[r,i] == '_':
                    i += 1
                    o_count = 0
                    x_count = 0
        return 'Ongoing'

    def check_diag_lupper(self):
        x_count = 0
        o_count = 0
        for r in range(self.rows - 1 - (abs(self.rows - self.cols)),-1,-1):
            i = r
            o_count = 0
            x_count = 0
            #print (i)
            for c in range(self.cols - (self.cols - 1 - r)):
                #print ("coord: %d,%d" % (i,c))
                if self.board[i,c] == 'X'  and c <= self.cols - 1:
                    i -= 1
                    x_count += 1
                    o_count = 0
                    if x_count >= self.game_win: 
                        return 'Xs'
                elif self.board[i,c] == 'O'  and c <= self.cols - 1:
                    i -= 1
                    o_count += 1
                    x_count = 0
                    if o_count >= self.game_win: 
                        return 'Os'
                else:
                    i -= 1
                    o_count = 0
                    x_count = 0
        return 'Ongoing'

    def check_diag_lower(self):
        x_count = 0
        o_count = 0
        for c in range(1, self.cols):
            i = c
            o_count = 0
            x_count = 0
            #print (i)
            for r in range(self.rows - 1, -1 + c, -1):
                #print ("coord: %d,%d" % (r,i))
                if self.board[r,i] == 'X'  and c <= self.cols - 1:
                    i += 1
                    x_count += 1
                    o_count = 0
                    if x_count >= self.game_win: 
                        return 'Xs'
                elif self.board[r,i] == 'O'  and c <= self.cols - 1:
                    i += 1
                    o_count += 1
                    x_count = 0
                    if o_count >= self.game_win: 
                        return 'Os'
                else:
                    i += 1
                    o_count = 0
                    x_count = 0
        return 'Ongoing'

        for i, arg in enumerate(sys.argv):
            if arg == "-c":
                cols = int(sys.argv[i + 1])
            elif arg == "-r":
                rows = int(sys.argv[i + 1])
            elif arg == "-w":
                game_win = int(sys.argv[i + 1])
            elif arg == "-t":
                if (sys.argv[i + 1] == 'X' or sys.argv[i + 1] == 'O'):
                    turn = sys.argv[i + 1]

def init_board(rows,cols):
    board = {}
    for r in range(rows):
        for c in range(cols):
            board[r,c] = '_'
    return board

def translate_cmd(input):
    for i in range(2):
        if i == 0:
            hold1 = alphabet_string.index(input[0])
        else:
            hold2 = int(input[i]) - 1
    return (hold1, hold2)

def set_board(self,cmd):
    if self.board[cmd] == '_':
        self.board[cmd] = self.turn
        return self.board, True
    else:
        print("Can't overwrite cell with value")
        return self.board, False

def check_draw(game):
    for k,v in sorted(game.board):
        if game.board[k,v] == '_':
            return False
    return True

bot = 'O'
player = 'X'
def compMove(game):
    bestScore = -1000
    bestMove = 0

    for r,c in sorted(game.board):
        if (game.board[r,c] == '_'):  
            game.board[r,c] = bot
            score = minimax(game,0,False)
            game.board[r,c] = '_'
            if (score > bestScore):
                    bestScore = score
                    bestMove = r,c
    set_board(game,bestMove)
    return

def minimax(game,depth, isMaximizing):
    if check_draw(game):
        return 0
    elif status(game) == bot:
        return 100
    elif status(game) == player:
        return -100
    if isMaximizing:
        bestScore = -1000

        for r,c in sorted(game.board):
            if (game.board[r,c] == '_'):  
                game.board[r,c] = bot
                score = minimax(game,0,False)
                game.board[r,c] = '_'
                if (score > bestScore):
                        bestScore = score
        return bestScore
    
    else:
        bestScore = 800

        for r,c in sorted(game.board):
            if (game.board[r,c] == '_'):  
                game.board[r,c] = player
                score = minimax(game, depth + 1, True)
                game.board[r,c] = '_'
                if (score < bestScore):
                    bestScore = score
        return bestScore


def status(game):
    par1 = game.check_diag_rupper()
    par2 = game.check_diag_rower()
    par3 = game.check_diag_lupper()
    par4 = game.check_diag_lower()
    par5 = game.check_cols()
    par6 = game.check_rows()
    if (par1 == 'Os') or (par2 == 'Os') or (par3 == 'Os') or (par4 == 'Os') or (par5 == 'Os') or (par6 == 'Os'):
        return 'O'
    elif (par1 == 'Xs') or (par2 == 'Xs') or (par3 == 'Xs') or (par4 == 'Xs') or (par5 == 'Xs') or (par6 == 'Xs'):
        return 'X'
    elif(check_draw(game)):
        return
    else:
        return 'Ongoing'

if __name__ == "__main__":
    cols = 3
    rows = 3
    game_win = 3
    turn = 'O'
    game = Game(turn, init_board(rows,cols), rows,cols, game_win)
    mode = raw_input("Would you like to play with 1 or 2 players?")
    if (mode == '2'):
        while(status(game) == 'Ongoing'):
            clearConsole = lambda: os.system('clear')
            clearConsole()
            game.show_board()
            if game.turn == 'O':
                game.say_turn()
                input = raw_input("Enter coordinates:")
                cmd = translate_cmd(input)
                board, bool = set_board(game,cmd)
                if (bool): 
                    turn = game.change_turn()
                game = Game(turn, board, rows,cols, game_win)
            else:
                game.say_turn()
                input = raw_input()
                cmd = translate_cmd(input)
                board, bool = set_board(game,cmd) 
                if (bool): 
                    turn = game.change_turn()
                game = Game(turn, board, rows,cols, game_win)
        game.show_board()     
        if (status(game) == 'O'):
            print("Congratulations, Circles Win")
        elif (status(game) == 'X'):
            print("Congratulations, Xs Win")
        elif (check_draw(game)):
            print("Draw")
    else:
        while status(game) == 'Ongoing':
            clearConsole = lambda: os.system('clear')
            clearConsole()
            if turn == 'O':
                compMove(game)
                turn = game.change_turn()
            else:
                game.show_board()
                game.say_turn()
                input = raw_input("Enter coordinates:")
                cmd = translate_cmd(input)
                board, bool = set_board(game,cmd)
                if (bool): 
                    turn = game.change_turn()
                game = Game(turn, board, rows,cols, game_win)
        if (status(game) == 'O'):
            game.show_board()
            print("Congratulations, Circles Win")
        elif (status(game) == 'X'):
            game.show_board()
            print("Congratulations, Xs Win")
        elif (check_draw(game)):
            game.show_board()
            print("Draw")