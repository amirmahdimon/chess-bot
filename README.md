# ♟️ Chess Best Move Finder (Using Stockfish)

This Python script allows you to input any **FEN (Forsyth–Edwards Notation)** string and get the **best move suggestion** using the **Stockfish chess engine**.

---

## 📦 Features

- Accepts any valid FEN position.
- Returns the best move using Stockfish (in both SAN and UCI formats).
- Simple CLI-based interface.
- Great for testing or learning from engine suggestions.

---

## 🚀 Requirements

- Python 3.6 or newer  
- [Stockfish Chess Engine](https://stockfishchess.org/download/)
- Python libraries:
  - `chess` (install via pip)

---

## 📥 Installation

1. **Download or clone this repository:**

   ```bash
   git clone https://github.com/amirmahdimon/chess-bot.git
   cd chess-best-m

2. **Install dependencies:**
   ```bash
   pip install chess
3. **Download and install Stockfish:**
- Go to Stockfish Downloads
- Download the version for your OS
- Extract it and note the path to the executable file
## ⚙️ Configuration
Open the script and modify the following line to match your Stockfish path:
- stockfish_path = "C:/Program Files/stockfish/stockfish-windows-x86-64-avx2.exe"
Make sure the path is correct and points to the stockfish executable.

## 🧠 How to Use
Run the script:
- python best_move_finder.py
- You'll see: 
Welcome! Paste a FEN string below to get the best move.
Type 'exit' to quit.
Example input:

Enter FEN: r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 2 4
Output: 
Best move: O-O (UCI format: e1g1)

## ❌ Exiting
To exit the program at any time, simply type: exit

## 📝 Notes
The script uses a 1-second limit for Stockfish to calculate the best move.

Invalid FEN strings will show a warning and prompt you again.

🧑‍💻 Author
Created by Amirmahdimon(Monty)
Feel free to contribute, report issues, or suggest improvements!


