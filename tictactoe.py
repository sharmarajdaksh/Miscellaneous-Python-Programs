#!/usr/bin/env python3

import os # only for clearing screen

##### GLOBAL DECLARATIONS #####

Edge = 3
Size = Edge**2
list = [" " for x in range(0, Size)]
#gives 'a' for the matrix of size (a x a) and the number of elements in 'list'
Turn = 0
# Turn = 1 implies Player2 turn; Turn = 2 implies Player1 turn
turnCount = 0
#count of the number of turns

###############################################################################

def getTurn():
# returns 0 if it is player1's turn and 1 if it is player2's turn
    global Turn
    return Turn

###############################################################################

def printBoard():
# prints the current status of the Board
    for i in range(0, Size, Edge):
        print(" ", list[i], end = "")
        for j in range(i + 1, i + Edge):
            print(' | ', list[j], end = "")
        print("")
        if i != (Size - Edge):
            for j in range(0, Edge - 1):
                print("-------", end = "")
            print("")

###############################################################################

def markBoard(var):
# marks the correct position with the correct suymbol
    global Turn, turnCount

    if Turn == 1:
        list[var] = "O"
        Turn = 0
    else:
        list[var] = "X"
        Turn = 1

    turnCount += 1

###############################################################################

def fullBoard():
# checks if board is full
    return turnCount == Size

###############################################################################

def returnFlag():
# returns the player number of the winner
        if getTurn():
            return 1
        else:
            return 2

###############################################################################

def checkStatus():
# return 1 or 2 if that player has won, else returns 0
    flag = 0

    diagonal = [x for x in range(0, Size, Edge + 1)]
    # print(diagonal)
    # check the diagonal WORKING
    if list[0] != " ":
        for i in diagonal:
            if list[0] == list[i]:
                flag = 1
            else:
                flag = 0
                break
        if flag:
            return returnFlag()

    crossdiagonal = [x for x in range(Edge - 1, Size - Edge + 1, Edge - 1)]
    # print(crossdiagonal)
    # check the crossdiagonal WORKING
    if list[Edge - 1] != " ":
        for i in crossdiagonal:
            if list[Edge - 1] == list[i]:
                flag = 1
            else:
                flag = 0
                break
        if flag:
            return returnFlag()

    for i in range(0, Edge):
    # check each column WORKING
        column = [x for x in range(i, Size, Edge)]
        # print("COLUMN: ", column)
        if list[i] != " ":
            for j in column:
                if list[i] == list[j]:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag:
                return returnFlag()

    for i in range(0, Size, Edge):
    # check each row WORKING
        row = [x for x in range(i, i + Edge)]
        # print("ROW: ", row)
        if list[i] != " ":
            for j in row:
                if list[i] == list[j]:
                    flag = 1
                else:
                    flag = 0
                    break
        if flag:
            return returnFlag()

    if not flag:
        return 0

###############################################################################

while True:

    os.system('clear')
    printBoard()

    status = checkStatus()
    if status:
        print("Player ", status, " has won!")
        break

    if fullBoard():
        print("GAME OVER!\nIt's a draw! :D")
        break

    print("Player ", getTurn() + 1, "enter position(1-", Size, "): ")
    mark = int(input()) - 1

    if (list[mark] != " ") or (mark not in range(0, Size)):
        #print("Choose a valid, unmarked position!")
        continue

    markBoard(mark)
