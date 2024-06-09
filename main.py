import tkinter as tk
from PIL import Image, ImageTk
import pygetwindow as gw
import time
import pygame
import sys

pygame.init()

root = tk.Tk()
root.withdraw()


class windowClass:
    GRAVITY = 2
    MOMENTUM = 40
    DRAG = 1
    TOP = 500
    BOTTOM = -100
    
    def __init__(self):
        self.calcWindow=tk.Toplevel()
        self.calcWindow.title("Calculator")
        self.calcWindow.geometry("640x480")

        #configure inputs
        self.calcWindow.bind('<space>', self.press_space)
        self.calcWindow.bind('<a>', self.pressLeft)
        self.calcWindow.bind('<d>', self.pressRight)


        self.x, self.y = 100, 100
        self.inertiaX, self.inertiaY = 0, 0
        self.width, self.height = 640, 480

    def press_space(self, event):
        self.inertiaY -= self.MOMENTUM
        
    def pressRight(self, event):
        self.inertiaX += self.MOMENTUM

    def pressLeft(self, event):
        self.inertiaX -= self.MOMENTUM
    
    def update(self):

        self.y += self.inertiaY
        if(self.inertiaY != 0):
            if(self.inertiaY < 0):
                self.inertiaY += self.DRAG
            if(self.inertiaY > 0):
                self.inertiaY -= self.DRAG


        self.x += self.inertiaX
        if(self.inertiaX != 0):
            if(self.inertiaX < 0):
                self.inertiaX += self.DRAG
            if(self.inertiaX > 0):
                self.inertiaX -= self.DRAG

        self.inertiaY += self.GRAVITY

        if(self.y > self.TOP):
            self.y = self.TOP
            self.inertiaY = 0
        if(self.y < self.BOTTOM):
            self.y = self.BOTTOM
            self.inertiaY = 0

        # if(self.x > self.TOP):
        #     self.x = self.TOP
        #     self.inertiaX = 0
        # if(self.x < self.BOTTOM):
        #     self.x = self.BOTTOM
        #     self.inertiaX = 0

        self.calcWindow.geometry("640x480+"+ str(self.x) + "+" + str(self.y))
        print("640x480+"+ str(self.x) + "+" + str(self.y))

    

    

#title = 'Calc'
#game_window = gw.getWindowsWithTitle(title)[0]

running = True


windowObj = windowClass()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #update
    root.update_idletasks()
    root.update()
    
    windowObj.update()

    #move window
    
    


    #render


    #cap fps
    pygame.time.Clock().tick(30)



pygame.quit()
sys.exit()