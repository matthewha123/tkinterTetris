# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:56:20 2017

@author: matth
"""

import tkinter as tk

class Board(tk.Canvas):
    blockSideL = 25
    blocks = []
    c = {0:'white',1:'blue', 2:'red'}
    def __init__(self, w,h,master=None):
        super().__init__(master, width = w, height = h)
        self.pack()
        self.dim = [w,h]
        #self.makeGrid(int(w/25),int(h/25))
        self.makeGrid(8,6)
        self.drawBoard()
    def makeGrid(self,width,length):
        self.grid = []
        for y in range(length):
            row = []
            self.grid.append(row)
            for x in range(width):
                self.grid[y].append(0)
    def drawBoard(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                self.create_rectangle(x*self.blockSideL,(y)*self.blockSideL,(x+1)*self.blockSideL,(y+1)*self.blockSideL, outline = 'black', fill = self.c[self.grid[y][x]])
    
    #need to add logic to make every other square 0.
    #also todo, listen for keyboard press and also have an update function
    def placeBlock(self,Block):
#        if(not(Block in self.blocks)):
#            self.blocks.append(Block)
        self.grid[Block.getPos()[0]-1][Block.getPos()[1]-1] = Block.getColor()
        print(self.grid)
    def update(self):
#        for b in blocks:
#            placeBlock(b)
        self.drawBoard()
    def mainloop(self):
        super().mainloop()

class Block(object):
    #pos variable: pos[0] holds the row val, pos[1] holds the column val
    def __init__(self,coord,color):
        self.pos = coord
        self.color = color
    # need to add logic to prevent movement if the block is not white
    def mR(self, board):
        self.pos[1] += 1
        if(self.pos[1] > board.dim[0]):
            self.pos[1] = board.dim[0]
    def mL(self,board):
        self.pos[1] += -1
        if(self.pos[1]<0):
            self.pos[1] = 0
    def mU(self,board):
        self.pos[0] += -1
        if(self.pos[0] < 0):
            self.pos[0] = 0
    def mD(self,board):
        self.pos[0] += 1
        if(self.pos[0] > board.dim[1]):
            self.pos[0] = board.dim[1]
    def getPos(self):
        return self.pos
    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color
    
#have a predefined array of different bArrays that correspond to different pieces
        #these bArrays will have one reference block, then, the other blocks will be set off of that block's position
        #these initial conditions are set once
        #these will be generated by a random generator function
#the piece class will store these arrays into a piece object
        #the piece class will have a rotation method and movement methods
class Piece(object):
    def __init__(self,bArr):
        self.p = bArr
    def cW(self):
        #every piece will move in a 
        pass
    def ccW(self):
        pass
        
        
root = tk.Tk()
app = Board(400,800,master = root)
b = Block([5,6],1)
print(b.getPos())
app.placeBlock(b)
app.drawBoard()
b.mR(app)
app.placeBlock(b)
app.drawBoard()
app.mainloop()