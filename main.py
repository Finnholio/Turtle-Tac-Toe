import turtle

BOARDSIZE = 30
SURFACE = Surface()

def drawBoard(boardState):
  pass


playing = True
playerPlaying = 1
boardState = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#main game loop

while playing:
  drawBoard(boardState)
  playerInput = getInput(playerPlaying)
  boardState = changeBoard(boardState, playerInput)
  hasPlayerWon = checkForWinner(boardState, playerInput)

  #change player
  playerPlaying *= -1


