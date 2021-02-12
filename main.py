

import pygame
import time


# starting pygame

# load image
pygame.init()
pygame.mouse.set_cursor("tic-tac-toe.png")
tictoe = pygame.image.load("tic.jfif")
pygame.display.set_icon(tictoe)
screen = pygame.display.set_mode([400,400])
white = [0, 255, 255]
red = [0, 0, 255]
screen.fill(white)
pygame.display.set_caption("The Toe")
turn = True
add = pygame.image.load("add.png")
minus = pygame.image.load("minus.png")
press = pygame.Rect(200, 100, 100, 100)
def image(image):
    py = pygame.transform.scale(image, (50, 50))
    return py


class Rectangle:
    def __init__(self, canvas, id, posS, posE, turn):
        self.canvas = canvas
        self.id = id
        self.posS = posS + 25
        self.posE = posE + 25
        self.Rect = pygame.Rect(posS, posE, 100, 100)
        self.used = False
        self.turn = turn
    def turns(self):
        if self.turn:
            self.turn = False
            print("turns is false")
        else:
            self.turn = True
            print("turns is true")
        print("change turn " + str(self.turn))
        return self.turn



    def create(self):
        pygame.draw.rect(self.canvas, red, self.Rect, 1) # change
        pygame.display.flip()
        pygame.display.update()
        print("i am " + str(self.id))
        print("I am @ " + str(self.posS) + "    " + str(self.posE))


    def hit(self):
       if self.used == False:
            time.sleep(0.2)
            if self.Rect.collidepoint(pygame.mouse.get_pos()): # change
                if self.turn == True:
                    time.sleep(0.4)
                    self.canvas.blit(image(add), (self.posS, self.posE))
                    self.used = True
                    print("Plus Moved")

                else:
                    time.sleep(0.1)
                    self.canvas.blit(image(minus), (self.posS, self.posE))
                    self.used = True
                    print("Minus Moved")
                return True





r1 = Rectangle(screen, 1, 50, 50, True)
r1.create()
r2 = Rectangle(screen, 2, 150, 50, True)
r2.create()
r3 = Rectangle(screen, 3, 250, 50, True)
r3.create()
r4 = Rectangle(screen, 4, 50, 150, True)
r4.create()
r5 = Rectangle(screen, 5, 150, 150, True)
r5.create()
r6 = Rectangle(screen, 6, 250, 150, True)
r6.create()
r7 = Rectangle(screen, 7, 50, 250, True)
r7.create()
r8 = Rectangle(screen, 8, 150, 250, True)
r8.create()
r9 = Rectangle(screen, 9, 250, 250, True)
r9.create()
# Drawing Rectangle
# game loop
def changeTurn():
    r1.turns()
    r2.turns()
    r3.turns()
    r4.turns()
    r5.turns()
    r6.turns()
    r7.turns()
    r8.turns()
    r9.turns()




while True:
    if r1.hit():
        changeTurn()
    elif r2.hit():
        changeTurn()
    elif r3.hit():
        changeTurn()
    elif r3.hit():
        changeTurn()
    elif r4.hit():
        changeTurn()
    elif r5.hit():
        changeTurn()
    elif r6.hit():
        changeTurn()
    elif r7.hit():
        changeTurn()
    elif r8.hit():
        changeTurn()
    elif r9.hit():
        changeTurn()


    for event in pygame.event.get():
        print(pygame.mouse.get_pos())
        if event.type == pygame.QUIT:
            # stops pygame
            pygame.quit()
            # stops program
            quit()
    pygame.display.flip()
    pygame.display.update()
pygame.quit()

