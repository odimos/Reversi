from player import *
from board import *
import argparse

def game(method1, method2, depth1, depth2, size, eval1, eval2, isTest):
    player_1 = Player(PLAYER_X, method1, depth1, eval1)
    player_2 = Player(PLAYER_O , method2, depth2, eval2)
    Board.SIZE = size
    board = Board( player_1, player_2)
    while True:
        if not isTest: 
            print_table(board.table, board.SIZE)
            print(f"\nits {board.players_turn.player_letter} turn")

        board.nextMove(isTest)

        if board.is_game_over():
            if isTest : return board.getResult()
            print_table(board.table, board.SIZE)
            return board.printResult()
            
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--size", type=int, default=8)
    args = parser.parse_args()
    SIZE = args.size

    players_turn = int(input("Players turn. Enter 1 if you want to go first, 2 to go second: "))
    MAX_DEPTH = int(input("Enter the maximum search depth for the minmax algorithm: "))

    if players_turn == 1:
        method1 = 'human'
        method2 = 'min_max'
    else :
        method1 = 'min_max'
        method2 = 'human'

    game(method1,method2, MAX_DEPTH, MAX_DEPTH, SIZE, "evaluate2", 'evaluate2', False)
