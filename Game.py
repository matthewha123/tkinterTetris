# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 12:54:57 2s017

@author: matth
"""
import tkinter as tk
import block

BLOCK_SIZE = 25
WIDTH = 250
HEIGHT = 500
   
            
def keyPressed(event,p):
    if(event.keysym == 'Right'):
        for b in p.blocks:
            b.move('r',board,p)
    if(event.keysym == 'Left'):
        for b in p.blocks:
            b.move('l',board,p)
    if(event.keysym == 'Down'):
        for b in p.blocks:
            b.move('d',board,p)
    if(event.keysym == 'Up'):
        for b in p.blocks:
            b.move('u',board,p)

    
def timerFired(board):
    delay = 250 # in ms
    board.after(delay,timerFired,board)
def drawGrid(board):
    for x in range(WIDTH//BLOCK_SIZE):
        for y in range(HEIGHT//BLOCK_SIZE):
            board.create_rectangle(x*BLOCK_SIZE, y*BLOCK_SIZE, (x+1)*BLOCK_SIZE, (y+1)*BLOCK_SIZE, outline = 'black', fill = 'white',tag = 'grid')
            
root = tk.Tk()
board = tk.Canvas(root, width = WIDTH, height = HEIGHT)
board.pack()
drawGrid(board)
#print(board.find_withtag('grid'))

#print(set(board.find_overlapping(1*(BLOCK_SIZE)+(BLOCK_SIZE/4),0*(BLOCK_SIZE)+(BLOCK_SIZE/4),1*(BLOCK_SIZE)+(BLOCK_SIZE-BLOCK_SIZE/4),0*(BLOCK_SIZE) + (BLOCK_SIZE-BLOCK_SIZE/4))) - set(board.find_withtag('blue')))
timerFired(board)

d = block.Block(0,0,'#551a8b',board)
c = block.Block(2,2,'red',board)
p = block.Piece('T', 6,board)
root.bind('<Key>',lambda event: keyPressed(event,p))
board.mainloop()
