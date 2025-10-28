# tic-tac-toe-in-python

a beginner console-based tic-tac-toe game written in python.  
originally made for my first semester CSE101 project, later upgraded with a rule-based ai opponent.

[`dummy_tic_tac_toe.py`](./dummy_tic_tac_toe.py): the original version, computer plays randomly 

[`ai_tic_tac_toe.py`](./ai_tic_tac_toe.py): new version with an ai opponent

# 🧠 about the AI

the ai in `ai_tic_tac_toe.py` is a simple rule-based system, not a perfect minimax ai.  
It tries to:
1. win if it can
2. block the player's winning move
3. prefer center or corners if available
4. otherwise pick a random empty cell
5. sometimes make random mistakes

the goal was to make it feel more human and unpredictable, not unbeatable.

## how to play
- you are X, the computer is O.  
- use row number and column letter for inputs like 1a, 2b, 3c to make your move.  
- to exit at any time, enter 00.

