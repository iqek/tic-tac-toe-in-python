import random

print("Welcome to Game of Tic-Tac-Toe (with AI)")
print("By Ipek Celik")


B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
moves = []

def playerinput(pmove):
    if pmove[0] not in "123" or pmove[1] not in "abc":
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
            if B[i][0] == 1:
                print("Congratulations! You Win!")
                return True
            elif B[i][0] == 2:
                print("Game Over. I Win!")
                return True
    for j in range(3):
        if B[0][j] == B[1][j] == B[2][j] != 0:
            if B[0][j] == 1:
                print("Congratulations! You Win!")
                return True
            elif B[0][j] == 2:
                print("Game Over. I Win!")
                return True
    if B[0][0] == B[1][1] == B[2][2] != 0:
        if B[0][0] == 1:
            print("Congratulations! You Win!")
            return True
        elif B[0][0] == 2:
            print("Game Over. I Win!")
            return True
    if B[0][2] == B[1][1] == B[2][0] != 0:
        if B[0][2] == 1:
            print("Congratulations! You Win!")
            return True
        elif B[0][2] == 2:
            print("Game Over. I Win!")
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

#ai
def ai_move():
    if random.random() > 0.1:            #check for AI win with a 10% chance of making a mistake
        for row in range(3):
            for column in range(3):
                if B[row][column] == 0:
                    B[row][column] = 2
                    if check_win(2):
                        return
                    B[row][column] = 0

    if random.random() > 0.2:            #check for player blocks
        for row in range(3):
            for column in range(3):
                if B[row][column] == 0:
                    B[row][column] = 1
                    if check_win(1):
                        B[row][column] = 2
                        return
                    B[row][column] = 0

    if random.random() < 0.2:            #random/default moves (corners and center prioritized)
        possible = [(row, column) for row in range(3) for column in range(3) if B[row][column] == 0]
        if possible:
            row, column = random.choice(possible)
            B[row][column] = 2
            return

    if B[1][1] == 0:
        B[1][1] = 2
        return
    for (row, column) in [(0,0),(0,2),(2,0),(2,2)]:
        if B[row][column] == 0:
            B[row][column] = 2
            return

    possible = [(row, column) for row in range(3) for column in range(3) if B[row][column] == 0]
    if possible:
        row, column = random.choice(possible)
        B[row][column] = 2

def check_win(player):
    for i in range(3):
        if B[i][0] == B[i][1] == B[i][2] == player:
            return True
    for j in range(3):
        if B[0][j] == B[1][j] == B[2][j] == player:
            return True
    if B[0][0] == B[1][1] == B[2][2] == player:
        return True
    if B[0][2] == B[1][1] == B[2][0] == player:
        return True
    return False



turn = random.randint(1, 2)
while True:
    board()
    if wintie():
        break

    if turn == 2:
        ai_move()
        print("AI has made its move.")
        turn = 1

    elif turn == 1:
        pmove = input("Your Move (Enter 00 to Exit): ")
        if pmove in moves:
            print("That cell is already full. Try Again.")
        elif pmove == "00":
            print("Thank you for playing Tic-Tac-Toe")
            break
        elif playerinput(pmove):
            turn = 2
            moves.append(pmove)
        else:
            print("Invalid Move. Try Again.")
