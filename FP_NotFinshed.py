import pygame
import random
import sys
import copy

display_width = 600
display_height = 600

Columns = 7
Rows = 7
SizeOfSlot = 64

NumberOfEmoji = 5

#RBG colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


up = 'up'
down = 'down'
left = 'left'
right = 'right'

EmptySpace = -1

def Initialization():
    pygame.init()
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Emoji Blitz')

    #Resize to fit slot
    Emojis = []
    for i in range(1,NumberOfEmoji + 1):
        EmojiImage = pygame.image.load('Emoji%s.png' % i)
        if EmojiImage.get_size() != (SizeOfSlot, SizeOfSlot):
            EmojiImage = pygame.transform.smoothscale(EmojiImage, (SizeOfSlot,SizeOfSlot))
        Emojis.append(EmojiImage)


    while True:
        runGame()

    def runGame():
        Board = EmptyBoard()

        while True:
            gameDisplay.fill(White)
            Board(Board)
            pygame.display.update()
            FPSCLOCK.tick(FPS)


def Swapping(Board, FirstEmoji, SecondEmoji):
    Emoji1 = {'imageNum': Board[FirstEmoji['x']][FirstEmoji['y']],'x' : FirstEmoji['x'], 'y': FirstEmoji['y']}
    Emoji2 = {'imageNum': Board[SecondEmoji['x']][SecondEmoji['y']],'x' : SecondEmoji['x'], 'y': SecondEmoji['y']}
    if Emoji1['x'] == Emoji2['x'] + 1 and Emoji1['y'] == Emoji2['y']:
        Emoji1['direction'] = left
        Emoji2['direction'] = right
    if Emoji1['x'] == Emoji2['x'] - 1 and Emoji1['y'] == Emoji2['y']:
        Emoji1['direction'] = right
        Emoji2['direction'] = left
    if Emoji1['y'] == Emoji2['y'] + 1 and Emoji1['x'] == Emoji2['x']:
        Emoji1['direction'] = up
        Emoji2['direction'] = down
    if Emoji1['y'] == Emoji2['y'] + 1 and Emoji1['x'] == Emoji2['x']:
        Emoji1['direction'] = down
        Emoji2['direction'] = up
    else:
        return None, None
    return Emoji1, Emoji2
        
def EmptyBoard():
    board = []
    for i in range(Columns):
        board.append([EmptySpace] * Rows)
    return board


def Rec():
    
def Board():
    for x in range(Columns):
        for y in range(Rows):
            pygame.draw.rec(gameDisplay, white, Rec[x][y], 1)
            EmojiDraw = board[x][y]
            if EmojiDraw != EmptySpace:
                gameDiaplay.blit(Emojis[EmojiDraw],Rec[x][y])
    


#runGame()
#Initialization()
Board()

    
    

                





    
