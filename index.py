import chess
import chess.engine

import sys

STOCKFISH_PATH = 'STOCKFISH_PATH'

board = chess.Board()

with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:

    while not board.is_game_over():
        user_input = input("Your move (SAN or UCI): ").strip()

        if user_input == 'resign':
            sys.exit('Game Over! Result: 0-1')

        move = None

        # Try SAN first
        try:
            move = board.parse_san(user_input)
        except ValueError:
            pass

        # If SAN fails, try UCI
        if move is None:
            try:
                move = chess.Move.from_uci(user_input)
            except ValueError:
                pass

        # Check if move is legal
        if move not in board.legal_moves:
            print("Illegal move! Try again.")
            continue

        # Push user move
        board.push(move)

        # Check game over
        if board.is_game_over():
            break

        # Stockfish move
        stockans = engine.play(board, chess.engine.Limit(time=1))
        stockmove = stockans.move
        print(f"Stockfish plays: {board.san(stockmove)}")
        board.push(stockmove)

# Print final result
print(f"Game over! Result: {board.result()}")