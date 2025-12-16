import random

print("Welcome to Game of Tic-Tac-Toe")
print("By Ipek Celik")

B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
moves = []


def playerinput(pmove):
    if len(pmove) != 2 or pmove[0] not in "123" or pmove[1] not in "abc":
        return False
    columns = ["a", "b", "c"]
    row = int(pmove[0]) - 1
    column = columns.index(pmove[1])
    if B[row][column] != 0:
        return False
    B[row][column] = 1
    return True


def wintie():
    for i in range(3):
        if B[i][0] == B[i][1] == B[i][2] != 0:
            print("Congratulations! You Win!" if B[i][0] == 1 else "Game Over. I Win!")
            return True

    for j in range(3):
        if B[0][j] == B[1][j] == B[2][j] != 0:
            print("Congratulations! You Win!" if B[0][j] == 1 else "Game Over. I Win!")
            return True

    if B[0][0] == B[1][1] == B[2][2] != 0:
        print("Congratulations! You Win!" if B[0][0] == 1 else "Game Over. I Win!")
        return True

    if B[0][2] == B[1][1] == B[2][0] != 0:
        print("Congratulations! You Win!" if B[0][2] == 1 else "Game Over. I Win!")
        return True

    for row in range(3):
        for column in range(3):
            if B[row][column] == 0:
                return False

    print("It's a tie!")
    return True


def board():
    print("    |  a  |  b  |  c  |")
    print("----+-----+-----+-----|")
    for row in range(3):
        print(str(row + 1) + "  |", end=" ")
        for column in range(3):
            if B[row][column] == 1:
                print(" X ", end="  |")
            elif B[row][column] == 2:
                print(" O ", end="  |")
            else:
                print("   ", end="  |")
        print("\n----+-----+-----+-----|")


def evaluate():
    for i in range(3):
        if B[i][0] == B[i][1] == B[i][2]:
            if B[i][0] == 2:
                return 10
            elif B[i][0] == 1:
                return -10

    for j in range(3):
        if B[0][j] == B[1][j] == B[2][j]:
            if B[0][j] == 2:
                return 10
            elif B[0][j] == 1:
                return -10

    if B[0][0] == B[1][1] == B[2][2]:
        return 10 if B[0][0] == 2 else -10 if B[0][0] == 1 else 0

    if B[0][2] == B[1][1] == B[2][0]:
        return 10 if B[0][2] == 2 else -10 if B[0][2] == 1 else 0

    return 0


def is_moves_left():
    for row in range(3):
        for col in range(3):
            if B[row][col] == 0:
                return True
    return False


def minimax(is_max):
    score = evaluate()

    if score == 10 or score == -10:
        return score

    if not is_moves_left():
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if B[i][j] == 0:
                    B[i][j] = 2
                    best = max(best, minimax(False))
                    B[i][j] = 0
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if B[i][j] == 0:
                    B[i][j] = 1
                    best = min(best, minimax(True))
                    B[i][j] = 0
        return best


def best_move():
    best_val = -1000
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if B[i][j] == 0:
                B[i][j] = 2
                move_val = minimax(False)
                B[i][j] = 0

                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)

    return move


turn = random.randint(1, 2)

while True:
    board()
    if wintie():
        break

    if turn == 2:
        row, column = best_move()
        B[row][column] = 2
        turn = 1

    else:
        pmove = input("Your Move (Enter 00 to Exit): ")
        if pmove == "00":
            print("Thank you for playing Tic-Tac-Toe")
            break
        elif pmove in moves:
            print("That cell is already full. Try Again.")
        elif playerinput(pmove):
            turn = 2
        else:
            print("Invalid Move. Try Again.")
        moves.append(pmove)