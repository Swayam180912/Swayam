import chess
import chess.engine

import sys

# Standard Algebric Notation (SAN)
# Universal Chess Interface (UCI)

# Download Stockfish from https://stockfishchess.org/download/

with chess.engine.SimpleEngine.popen_uci("STOCKFISH") as engine:
    board = chess.Board()
    result = engine.analyse(board, chess.engine.Limit(depth=15))

    result = str(result["score"]).replace('PovScore(', '').replace('(', ',').replace('', '').replace(')', '').replace(' ', '')

    unit, eval, color = result.split(',')

    moves = []

    while True:
        move = input("move: ")

        try:
            chess.Move.from_san("move")
        except:
            sys.exit('Please enter a Valid mmove')

        moves.append(move)