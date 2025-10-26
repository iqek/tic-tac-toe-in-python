# tic-tac-toe-in-python

a simple console-based tic-tac-toe game written in python.  
originally developed as my **first semester CSE101 project**, later upgraded with a **rule-based AI** opponent.

[`dummy_tic_tac_toe.py`](./dummy_tic_tac_toe.py): the original version, computer plays randomly 

[`ai_tic_tac_toe.py`](./ai_tic_tac_toe.py): enhanced version with a simple and human-like AI opponent
<br><br>
## 🧠 about the AI

the AI in `ai_tic_tac_toe.py` is a **simple rule-based system**, not a perfect minimax AI.  
It tries to:
1. win if it can
2. block the player's winning move
3. prefer center or corners if available
4. otherwise pick a random empty cell
5. sometimes make random mistakes

the goal was to make it feel more **human** and **unpredictable**, not unbeatable.
<br><br>
## how to play

- you play as **X**, and the computer plays as **O**.  
- use row number and column letter for inputs like 1a, 2b, 3c to make your move.  
- to exit at any time, enter 00.

