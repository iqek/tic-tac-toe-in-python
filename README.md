# tic-tac-toe-in-python

a simple console-based tic-tac-toe game written in python.  
originally developed as my **first semester CSE101 project**, later upgraded with a **rule-based AI** opponent.

---

## 📂 Project Files
[`dummy_tic_tac_toe_.py`](./dummy_tic_tac_toe.py): the original version, computer plays randomly 

[`ai_tic_tac_toe.py`](./ai_tic_tac_toe.py): enhanced version with a simple and human-like AI opponent
<br><br>
## 🧠 About the AI

the AI in `tic_tac_toe_ai.py` is a **simple rule-based system**, not a perfect minimax AI.
it tries to:
1. win if it can
2. block the player's winning move
3. prefer center or corners if available
4. otherwise pick a random empty cell
5. sometimes make random mistakes

the goal was to make it feel more **human** and **unpredictable**, not unbeatable.  
as the random mistakes are what keeps the game interesting.
<br><br>
## 🕹️ How to Play

you play as **X**, and the computer plays as **O**.  
use row number and column letter for inputs like 1a, 2b, 3c to make your move.  
to exit at any time, enter 00.  
invalid or already filled cells will be rejected.  
the game ends when either player wins or when the board is full (tie).  

