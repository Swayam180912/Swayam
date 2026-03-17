import chess

board = chess.Board()

engine = chess.engine.SimpleEngine.popen_uci(
    "C:/Users/thakkars/Desktop/stockfish/stockfish-windows-x86-64-avx2.exe"
)

board = chess.Board()
result = engine.analyse(board, chess.engine.Limit(depth=10))
print(result["score"].white().score())

engine.quit()