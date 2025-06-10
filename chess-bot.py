import chess
import chess.engine

# مسیر Stockfish
stockfish_path = "C:/Program Files/stockfish/stockfish-windows-x86-64-avx2.exe"

# ساخت تخته شطرنج
board = chess.Board()

# اتصال به موتور Stockfish
engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)

def get_best_move(fen):
    board.set_fen(fen)
    result = engine.play(board, chess.engine.Limit(time=1.0))
    best_move = result.move
    return best_move

def main():
    print("Welcome! Paste a FEN string below to get the best move.")
    print("Type 'exit' to quit.\n")

    while True:
        fen = input("Enter FEN: ")
        if fen.strip().lower() == "exit":
            break
        try:
            best_move = get_best_move(fen)
            print(f"Best move: {board.san(best_move)} (UCI format: {best_move})\n")
        except ValueError:
            print("Invalid FEN! Please try again.\n")

if __name__ == "__main__":
    try:
        main()
    finally:
        engine.quit()
