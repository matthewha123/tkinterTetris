# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:58:52 2017

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