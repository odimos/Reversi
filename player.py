import math
import random
from board import *

class Player:
    def __init__(self,player_letter,  method=None, max_depth=0, eval_method="evaluate2" ):
        self.player_letter = player_letter
        self.method = method
        self.max_depth = max_depth
        self.evaluate = eval_method
        if method == 'human': self.getMove = self.humanInput
        elif method == 'min_max': self.getMove = self.min_max
        elif method == 'min_max_': self.getMove = self.min_max
        elif method == 'firstOne': self.getMove = self.firstOne
        elif method == 'randomMove': self.getMove = self.randomMove
        elif method == 'instaMax': self.getMove = self.instaMax
        elif method == 'instaMax_': self.getMove = self.instaMax
        elif method == 'instaMaxRandom': self.getMove = self.instaMaxRandom
        elif method == 'instaMaxRandom_': self.getMove = self.instaMaxRandom
        elif method == 'randomMove2' : self.getMove = self.randomMove2

    def min_max(self, board, possibleMoves):
        evaluation, best_move = self.max_minmax(board, 0, -math.inf, math.inf) 
        return best_move

    def max_minmax(self, board, depth, alpha, beta):
        if board.isTerminal():
            return getattr(board, self.evaluate)(self.player_letter, True), None
        if depth == self.max_depth:
            return getattr(board, self.evaluate)(self.player_letter, False), None
        
        moves = board.allPossibleMoves(board.players_turn.player_letter)
        children = board.generateChildrenFromMoves(moves)
        max_eval = -math.inf
        move = None
        
        for child in children:
            eval, _ = self.min_minmax(child, depth + 1, alpha, beta)
            if eval > max_eval:
                max_eval = eval
                move = child.lastMove
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break
            
        return max_eval, move

    def min_minmax(self, board, depth, alpha, beta):

        if board.isTerminal():
            return getattr(board, self.evaluate)(self.player_letter, True), None
        if depth == self.max_depth:
            return getattr(board, self.evaluate)(self.player_letter, False), None
        
        moves = board.allPossibleMoves(board.players_turn.player_letter)
        children = board.generateChildrenFromMoves(moves)
        min_eval = math.inf
        move = None
        
        for child in children:
            eval, _ = self.max_minmax(child, depth + 1, alpha, beta)
            if eval < min_eval:
                min_eval = eval
                move = child.lastMove
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
            
        return min_eval, move
 
    # move selection method from user input
    def humanInput(self, board, possibleMoves):
        try:
            move_input = input(f"Enter your move {self.player_letter} (column and row separated by space): ")
            col, row = map(int, move_input.split())
            return (col,row)
        except ValueError:
            return (-1, -1)
            
    # Different move selection methods to compare with minmax
    def firstOne(self, board, possibleMoves):
        col, row = possibleMoves[0]
        return (col, row)
    def randomMove(self, board, possibleMoves):
        col, row = random.choice(possibleMoves)
        return (col, row)
    def randomMove2(self, board, possibleMoves):
        col, row = random.choice(possibleMoves)
        return (col, row)
    def instaMax(self, board, possibleMoves):
        children = board.generateChildrenFromMoves(possibleMoves)
        letter = self.player_letter 
        col, row = max(children, key=lambda child: getattr(child, self.evaluate)(letter, False)).lastMove
        return col, row
    
    def instaMaxRandom(self, board, possibleMoves):
        children = board.generateChildrenFromMoves(possibleMoves)
        letter = self.player_letter 
        max_score = max(getattr(child, self.evaluate)(letter, False) for child in children)
        best_children = [child for child in children if getattr(child, self.evaluate)(letter, False) == max_score]
        chosen_child = random.choice(best_children)
        return chosen_child.lastMove