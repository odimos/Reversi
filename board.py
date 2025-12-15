import copy

EMPTY_SYMBOL = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'


class Board:
    SIZE = 8 # Defult value
    def __init__(self,players_turn_1,players_turn_2, table=None):
        self.player_1 = players_turn_1
        self.player_2 = players_turn_2
        self.table = copy.deepcopy(table) if table else initializeBoard(Board.SIZE)
        self.players_turn = players_turn_1
        self.lastMove = None

    def otherPlayer(self, player):
        if player == self.player_1: return self.player_2
        return self.player_1

    def is_valid_move(self, player, row, col):
        # like the possible moves but stop sooner
        if self.table[row][col] != EMPTY_SYMBOL:
            return False
        
        opponent = otherSymbol(player)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  (-1, -1), (-1, 1), (1, -1), (1, 1)]  

        for dx, dy in directions:
            x, y = row + dx, col + dy
            has_opponent_piece = False

            while 0 <= x < Board.SIZE and 0 <= y < Board.SIZE and self.table[x][y] == opponent:
                has_opponent_piece = True
                x += dx
                y += dy

            if has_opponent_piece and 0 <= x < Board.SIZE and 0 <= y < Board.SIZE and self.table[x][y] == player:
                return True

        return False
    
    def is_game_over(self):
        if not self.has_valid_move(self.player_1.player_letter) and not self.has_valid_move(self.player_2.player_letter):
            return True
        return False

    def has_valid_move(self, player):
        for i in range(Board.SIZE):
            for j in range(Board.SIZE):
                if self.table[i][j] == EMPTY_SYMBOL and self.is_valid_move(player, i, j):
                    return True  # break
        return False

    def allPossibleMoves(self, player):
        moves = []
        for i in range(Board.SIZE):
            for j in range(Board.SIZE):
                toTurnedPieces=toTurn(j,i, player, self.table, Board.SIZE)
                if toTurnedPieces :            
                    moves.append( (j, i) )
        return moves
    
    
    def placeRaw(self, x, y):
        for piece in toTurn(x,y, self.players_turn.player_letter, self.table, Board.SIZE):
            self.table[piece[1]][piece[0]] = self.players_turn.player_letter
        self.table[y][x] = self.players_turn.player_letter

    def nextMove(self, isTest):
        possibleMoves = self.allPossibleMoves(self.players_turn.player_letter)
        if possibleMoves:
            move = self.players_turn.getMove(self, possibleMoves)
            if move in possibleMoves:
                x = move[0]
                y = move[1]
                self.placeRaw(x, y)
                self.players_turn = self.otherPlayer(self.players_turn)
                return True
            else :
                print(f"{self.players_turn.player_letter} -> ({move}) Invalid move, try again\n")
                return True
        else :
            # Empty move
            if not isTest: print(f"No valid moves for {self.players_turn.player_letter} ")
            self.players_turn = self.otherPlayer(self.players_turn)
            return False
    
    def isTerminal(self):
        return not self.allPossibleMoves(PLAYER_X) and not self.allPossibleMoves(PLAYER_O)

    def generateChildFromMove(self, x, y):
        newBoard = Board(self.player_1, self.player_2, self.table)
        newBoard.players_turn = self.players_turn
        newBoard.placeRaw(x, y)
        newBoard.lastMove = (x, y)
        newBoard.players_turn = self.otherPlayer(self.players_turn)
        return newBoard

    def generateEmptyMove(self):
        newBoard = Board(self.player_1, self.player_2, self.table)
        # empty move
        newBoard.players_turn = self.otherPlayer(self.players_turn)
        newBoard.lastMove = (-1, -1)
        return newBoard

    def generateChildrenFromMoves(self, possibleMoves):
        children = []
        if possibleMoves :  
            for move in possibleMoves:
                newChild = self.generateChildFromMove(move[0], move[1])
                children.append(newChild)
        else :
            newChild = self.generateEmptyMove()
            children.append(newChild)

        return children

    def evaluate(self, from_players_perspective, isKnownTerminal=False):
        oponent = otherSymbol(from_players_perspective)
        count_1 = 0
        count_2 = 0
        for i in range(Board.SIZE):
            for j in range(Board.SIZE):
                if from_players_perspective == self.table[i][j] : count_1 += 1
                elif oponent == self.table[i][j] : count_2 += 1

        if isKnownTerminal or self.is_game_over():
            if count_1 > count_2:
                return 1000
            elif count_2 > count_1 :
                return -1000
        return count_1 - count_2

    def calculateScore(self):
        count_1 = 0
        count_2 = 0
        for i in range(Board.SIZE):
            for j in range(Board.SIZE):
                if self.player_1.player_letter == self.table[i][j] : count_1 += 1
                elif self.player_2.player_letter == self.table[i][j] : count_2 += 1

        return count_1, count_2


    def printResult(self):
        player_1_score, player_2_score = self.calculateScore()
        print(f"Game Over!\n Score  {self.player_1.player_letter}:{player_1_score} - {self.player_2.player_letter}:{player_2_score}")

        if player_1_score > player_2_score :
            print(f" {self.player_1.player_letter} {self.player_1.method} Won Over {self.player_2.player_letter} {self.player_2.method} ")
        elif player_2_score > player_1_score:
            print(f" {self.player_2.player_letter} {self.player_2.method} Won Over {self.player_1.player_letter} {self.player_1.method} ")
        else:
            print(f" TIE! {self.player_1.player_letter} {self.player_1.method} tied with {self.player_2.player_letter} {self.player_2.method} ")
        
    def getResult(self):
        player_1_score, player_2_score = self.calculateScore()        
        if player_1_score > player_2_score:
            return self.player_1.method
        elif player_2_score > player_1_score:
            return self.player_2.method
        else:
            return 'tie'
    
    def evaluate2(self, from_players_perspective, endNode):
        oponent = otherSymbol(from_players_perspective)
        f1=0 # players pieces - oponent pieces
        f2=0 # players pieces on corners - oponent pieces on corners
        f3=0 # akraies positions

        corners = [(0, 0), (0, Board.SIZE - 1), (Board.SIZE - 1, 0), (Board.SIZE - 1, Board.SIZE - 1)]

        for i in range(Board.SIZE):
            for j in range(Board.SIZE):
                piece = self.table[i][j]
                if piece == from_players_perspective:
                    f1 += 1
                    if (i, j) in corners:
                        f2 += 1
                    elif i == 0 or i == Board.SIZE - 1 or j == 0 or j == Board.SIZE - 1:
                        f3 += 1
                elif piece == oponent:
                    f1 -= 1
                    if (i, j) in corners:
                        f2 -= 1
                    elif i == 0 or i == Board.SIZE - 1 or j == 0 or j == Board.SIZE - 1:
                        f3 -= 1

        if self.isTerminal(): # or endNode
            if f1 > 0 :
                return 1000
            elif f1 < 0 :
                return -1000
            else :
                return 0
            
        return f1 + 3*f2 + 2*f3


def otherSymbol(symbol):
    if symbol == PLAYER_X : return PLAYER_O
    else : return PLAYER_X

def initializeBoard(size):
    table = [ [ EMPTY_SYMBOL for __ in range(size) ] for _ in range(size) ]
    mid_down = int( size/2 ) - 1
    table[mid_down][mid_down] = PLAYER_X; table[mid_down+1][mid_down+1] = PLAYER_X; 
    table[mid_down][mid_down+1] = PLAYER_O; table[mid_down+1][mid_down] = PLAYER_O
    return table

def print_table(table, size):
    header_str = '  . '
    for header in range(size):
        header_str+=str(header)+" . "
    print(header_str)
    for index, row in enumerate(table):
        row_str = str(index)+' | ' + " | ".join(map(str, row)) +" |"
        print(row_str)

def toTurn(x,y, player, table, size):

    if table[y][x] != EMPTY_SYMBOL:
        return False

    toTurnPieces = []
    dir = [ (0,1),(1,0), (1,1), (0,-1),(-1,0), (-1,1), (1,-1), (-1,-1)  ]
    for direction in dir:
        now_x = x + direction[0]
        now_y = y  + direction[1]
        pieces_between = []

        while now_x >=0 and now_x < size and now_y >=0 and now_y < size :
            # same player, valid list
            if table[now_y][now_x] == player:
                toTurnPieces.extend(pieces_between)
                break
            elif table[now_y][now_x] == EMPTY_SYMBOL:
                break
            else :
                pieces_between.append((now_x, now_y))
                now_x = now_x + direction[0]
                now_y = now_y  + direction[1]

    return toTurnPieces    

def print_possible_moves(moves, table):
    table_copy = copy.deepcopy(table)
    for place in moves :
        table_copy[place[0]][place[1]] = '-'
    print_table(table_copy)
