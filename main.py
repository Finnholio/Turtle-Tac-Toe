#!/usr/bin/env python3

import pygame as p
import math

p.init()

BOARDSIZE = 700
SCREEN = p.display.set_mode([BOARDSIZE, BOARDSIZE])

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pointsForBoard = []

def drawBoard():
    #draw the tic tac toe board
    SCREEN.fill(WHITE)

    p.draw.line(SCREEN, BLACK, (BOARDSIZE/3, 0), (BOARDSIZE/3, BOARDSIZE), 5)
    p.draw.line(SCREEN, BLACK, (2*BOARDSIZE/3, 0), (2*BOARDSIZE/3, BOARDSIZE), 5)
    p.draw.line(SCREEN, BLACK, (0, BOARDSIZE/3), (BOARDSIZE, BOARDSIZE/3), 5)
    p.draw.line(SCREEN, BLACK, (0, 2*BOARDSIZE/3), (BOARDSIZE, 2*BOARDSIZE/3), 5)

def updateBoard(boardState):
    #make board
    drawBoard()

    #draw xs and os
    for i in range(len(boardState)):
        for j in range(len(boardState[i])):
            if boardState[i][j] == 1:
                drawX(BOARDSIZE/3 * i, BOARDSIZE/3 * j)
            elif boardState[i][j] == -1:
                drawO(BOARDSIZE/3 * i, BOARDSIZE/3 * j)

    p.display.update()

def getInput(currentPlayer):
    #set default space
    inputedSpace = [-1.0, -1.0]

    #check for button being pressed
    events = p.event.get()
    for event in events:
        print("mouse pressed")
        if event.type == p.MOUSEBUTTONUP:
            mousePosition = p.mouse.get_pos()

            #get inputed space if mouse button pressed
            inputedSpace[0] = int(math.floor(mousePosition[0] / (BOARDSIZE/3)))
            inputedSpace[1] = int(math.floor(mousePosition[1] / (BOARDSIZE/3)))

    return inputedSpace

def changeBoard(boardState, currentPlayer, placeChanged):
    if placeChanged[0] != -1:
        newBoardState = boardState
        spotBeingChanged = newBoardState[placeChanged[0]][placeChanged[1]]

        if spotBeingChanged == 0:
            newBoardState[placeChanged[0]][placeChanged[1]] = currentPlayer
            return newBoardState


        else:
            print("rejected case 1")
            return boardState

    else:
        return boardState

def checkForWinner(boardState):
    for i in range(len(boardState)):
        #check verticle
        if boardState[i][0] == boardState[i][1] and boardState[i][1] == boardState[i][2]:
            return boardState[i][0]

        #check horizontal
        if boardState[0][i] == boardState[1][i] and boardState[1][i] == boardState[2][i]:
            return boardState[i][0]

    #check diagonal
    if boardState[0][0] == boardState[1][1] and boardState[1][1] == boardState[2][2]:
        return boardState[i][0]

    if boardState[2][0] == boardState[1][1] and boardState[1][1] == boardState[0][2]:
        return boardState[i][0]

    return 0

def drawX(x, y):
    deadSpace = BOARDSIZE/3 * 1/5

    p.draw.line(SCREEN, BLACK, (x+deadSpace, y+deadSpace), (x+BOARDSIZE/3-deadSpace, y+BOARDSIZE/3-deadSpace), 5)
    p.draw.line(SCREEN, BLACK, (x+deadSpace, y+BOARDSIZE/3-deadSpace), (x+BOARDSIZE/3-deadSpace, y+deadSpace), 5)

def drawO(x, y):
    centerX = x + BOARDSIZE/6
    centerY = y + BOARDSIZE/6

    radius = BOARDSIZE/3 * 2/5

    p.draw.circle(SCREEN, BLACK, (centerX, centerY), radius, 5)

playing = True
playerPlaying = 1
boardState = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#main game loop
while playing:
    #update graphics
    updateBoard(boardState)

    #check for winner
    hasPlayerWon = checkForWinner(boardState)

    if hasPlayerWon != 0:
        playing = False

    #check to see if user quit game
    event = p.event.poll()
    if event.type == p.QUIT:
        break

    #get input and change board
    playerInput = getInput(playerPlaying)
    boardState = changeBoard(boardState, playerPlaying, playerInput)

    #change player
    if playerInput[0] != -1:
        playerPlaying = playerPlaying * -1







if hasPlayerWon != -2:
    print("player " + str(hasPlayerWon) + " has won!")
else:
    print("its a tie!")

p.quit()
