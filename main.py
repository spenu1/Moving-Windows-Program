import tkinter as tk
from PIL import Image, ImageTk
import pygetwindow as gw
import time
import pygame
import sys
import glob, os
from pathlib import Path

pygame.init()

root = tk.Tk()
root.withdraw()

class screenSizeClass:
    #variables
    GRAVITY = 0
    MOMENTUM = 100
    DRAG = 1000
    #boundaries
    TOP = -10000
    BOTTOM = 90000
    LEFT = -200000
    RIGHT = 180000
    #dimensions
    WIDTH = 50
    HEIGHT = 50
    
    def __init__(self):
        


        self.calcWindow=tk.Toplevel()
        self.calcWindow.title("Calculator")
        self.calcWindow.geometry(str(self.WIDTH) + "x" + str(self.HEIGHT))
        self.calcWindow.attributes('-topmost',True)
        self.calcWindow.configure(bg="red")

        #configure image
        self.calcWindow.overrideredirect(True)


        
        #configure inputs
        self.calcWindow.bind('<w>', self.pressUp)
        self.calcWindow.bind('<s>', self.pressDown)
        self.calcWindow.bind('<a>', self.pressLeft)
        self.calcWindow.bind('<d>', self.pressRight)
        self.calcWindow.bind('<Return>', self.pressEnter)

        self.set = False
        self.x, self.y = 100, 100
        self.inertiaX, self.inertiaY = 0, 0
        self.width, self.height = 640, 480

    def pressUp(self, event):
        self.inertiaY -= self.MOMENTUM
        
    def pressDown(self, event):
            self.inertiaY += self.MOMENTUM

    def pressRight(self, event):
        self.inertiaX += self.MOMENTUM

    def pressLeft(self, event):
        self.inertiaX -= self.MOMENTUM

    def pressEnter(self, event):
        self.set = True

    def destroySelf(self):
        self.destroy()
    
    def update(self):
        
        self.y += self.inertiaY
        if(self.inertiaY != 0):
            if(self.inertiaY < 0):
                self.inertiaY += self.DRAG
                if (self.inertiaY > 0):
                    self.inertiaY = 0
            if(self.inertiaY > 0):
                self.inertiaY -= self.DRAG
                if (self.inertiaY < 0):
                    self.inertiaY = 0


        self.x += self.inertiaX
        if(self.inertiaX != 0):
            if(self.inertiaX < 0):
                self.inertiaX += self.DRAG
                if (self.inertiaX > 0):
                    self.inertiaX = 0
            if(self.inertiaX > 0):
                self.inertiaX -= self.DRAG
                if (self.inertiaX < 0):
                    self.inertiaX = 0

        self.inertiaY += self.GRAVITY

        if(self.y < self.TOP):
            self.y = self.TOP
            self.inertiaY = self.inertiaY * -1
        if(self.y > self.BOTTOM):
            self.y = self.BOTTOM
            self.inertiaY = self.inertiaY * -1

        if(self.x < self.LEFT):
            self.x = self.LEFT
            self.inertiaX = self.inertiaX * -1
        if(self.x > self.RIGHT):
            self.x = self.RIGHT
            self.inertiaX = self.inertiaX * -1

    # if(self.x > self.TOP):
    #     self.x = self.TOP
    #     self.inertiaX = 0
    # if(self.x < self.BOTTOM):
    #     self.x = self.BOTTOM
    #     self.inertiaX = 0
        
        if (self.set == True):
            return self.x, self.y

        self.calcWindow.geometry(str(self.WIDTH) + "x" + str(self.HEIGHT) + "+" + str(self.x) + "+" + str(self.y))


class windowClass:
    #variables
    GRAVITY = 0
    MOMENTUM = 10
    DRAG = 0

    #dimensions
    WIDTH = 200
    HEIGHT = 200
    
    def __init__(self, filepath, top, bottom, left, right):
        


        self.calcWindow=tk.Toplevel()
        self.calcWindow.title("Calculator")
        self.calcWindow.geometry(str(self.WIDTH) + "x" + str(self.HEIGHT))
        self.calcWindow.attributes('-topmost',True)
        

        #configure image
        self.image = Image.open(filepath)
        self.image = self.image.resize((self.WIDTH, self.HEIGHT))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.calcWindow, image=self.photo, bg='#110101')

        self.calcWindow.wm_attributes("-transparentcolor", "#110101")
        self.calcWindow.overrideredirect(True)

        self.image_label.pack()
        
        #configure inputs
        self.calcWindow.bind('<w>', self.pressUp)
        self.calcWindow.bind('<s>', self.pressDown)
        self.calcWindow.bind('<a>', self.pressLeft)
        self.calcWindow.bind('<d>', self.pressRight)

        #boundaries
        self.TOP = top
        self.BOTTOM = bottom
        self.LEFT = left
        self.RIGHT = right

    

        self.x, self.y = int(((left-right)/2) + right), int(((bottom - top) / 2) + top)
        self.inertiaX, self.inertiaY = 0, 0
        self.width, self.height = 640, 480

    def pressUp(self, event):
        self.inertiaY -= self.MOMENTUM
        
    def pressDown(self, event):
            self.inertiaY += self.MOMENTUM

    def pressRight(self, event):
        self.inertiaX += self.MOMENTUM

    def pressLeft(self, event):
        self.inertiaX -= self.MOMENTUM
    
    def update(self):

        self.y += self.inertiaY
        if(self.inertiaY != 0):
            if(self.inertiaY < 0):
                self.inertiaY += self.DRAG
                if (self.inertiaY > 0):
                    self.inertiaY = 0
            if(self.inertiaY > 0):
                self.inertiaY -= self.DRAG
                if (self.inertiaY < 0):
                    self.inertiaY = 0


        self.x += self.inertiaX
        if(self.inertiaX != 0):
            if(self.inertiaX < 0):
                self.inertiaX += self.DRAG
                if (self.inertiaX > 0):
                    self.inertiaX = 0
            if(self.inertiaX > 0):
                self.inertiaX -= self.DRAG
                if (self.inertiaX < 0):
                    self.inertiaX = 0

        self.inertiaY += self.GRAVITY

        if(self.y < self.TOP):
            self.y = self.TOP
            self.inertiaY = self.inertiaY * -1
        if(self.y > self.BOTTOM):
            self.y = self.BOTTOM
            self.inertiaY = self.inertiaY * -1

        if(self.x < self.LEFT):
            self.x = self.LEFT
            self.inertiaX = self.inertiaX * -1
        if(self.x > self.RIGHT):
            self.x = self.RIGHT
            self.inertiaX = self.inertiaX * -1

        # if(self.x > self.TOP):
        #     self.x = self.TOP
        #     self.inertiaX = 0
        # if(self.x < self.BOTTOM):
        #     self.x = self.BOTTOM
        #     self.inertiaX = 0
            
        

        self.calcWindow.geometry(str(self.WIDTH) + "x" + str(self.HEIGHT) + "+" + str(self.x) + "+" + str(self.y))


    

    

#title = 'Calc'
#game_window = gw.getWindowsWithTitle(title)[0]

running = True

windowsImages = []
pathTmp = os.path.dirname(__file__)
    



scresize0 = screenSizeClass()

configuring = True
#up down left right
topMost = 0

top, bottom, left, right = 0,0,0,0

print("Configuring")
print("Move Square to Top of Your Screen")
while configuring:
    #update
    root.update_idletasks()
    root.update()
    if(topMost == 3):
        response = scresize3.update()
    elif(topMost == 2):
        response = scresize2.update()
    elif(topMost == 1):
        response = scresize1.update()
    elif(topMost == 0):
        response = scresize0.update()
    
    if(response != None):
        if(topMost == 3):
            right = response[0]
            configuring = False
        elif(topMost == 2):
            left = response[0]
            topMost = 3
            scresize3 = screenSizeClass()
            print("Set")
            print("Move Square to Right of Your Screen")
        elif(topMost == 1):
            bottom = response[1]
            topMost = 2
            scresize2 = screenSizeClass()
            print("Set")
            print("Move Square to Left of Your Screen")
        elif(topMost == 0):
            top = response[1]
            topMost = 1
            scresize1 = screenSizeClass()
            print("Set")
            print("Move Square to Bottom of Your Screen")

        # if(topMost != True):
        #     right = response[0]
        #     bottom = response[1]
        #     configuring = False
        # else:
        #     left = response[0]
        #     top = response[1]
        #     topMost = False
        #     scresize2 = screenSizeClass()
        #     print("Set")
        #     print("Move Square to Bottom Right of Your Screen")
        
    pygame.time.Clock().tick(30)

for widget in root.winfo_children():
    if isinstance(widget, tk.Toplevel):
        widget.destroy()

for file in os.listdir(pathTmp + "/pngs"):
         print(os.path.join(pathTmp, file))
         if (file.endswith(".png") or file.endswith(".jpg")):
             print(os.path.join(pathTmp, file))
             
             windowsImages.append(windowClass( (os.path.join(pathTmp + "/pngs", file)) , top, bottom, left, right))
            

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #update
    root.update_idletasks()
    root.update()

    

    for winImg in windowsImages:
        winImg.update()


    #move window
    
    
    


    #render


    #cap fps
    pygame.time.Clock().tick(30)


time.sleep(5)
pygame.quit()
sys.exit()