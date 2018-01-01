# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 12:54:57 2s017

@author: matth
"""
import tkinter as tk
import block
import random

BLOCK_SIZE = 25
WIDTH = 250
HEIGHT = 500
   
            
def keyPressed(event,p):
    if(event.keysym == 'Right'):
        p.move('r',1,0,board)
    if(event.keysym == 'Left'):
        p.move('l',-1,0,board)
    if(event.keysym == 'Down'):
        p.move('d',0,1,board)
    if(not(p.choice) == 'O'):
        if(event.keysym == 'q'):
            print('hi')
            p.rotate('ccw',board)
        if(event.keysym == 'e'):
            p.rotate('cw',board)
#    if(event.keysym == 'Up'):
#        p.move('u',0,-1,board)
    
def timerFired(board):
    global p
    delay = 500
    print(p.active)
    if(not p.active):
        p = genPiece(board,p)
    p.move('d',0,1,board)
    board.after(delay,timerFired,board)
def drawGrid(board):
    for x in range(WIDTH//BLOCK_SIZE):
        for y in range(HEIGHT//BLOCK_SIZE):
            board.create_rectangle(x*BLOCK_SIZE, y*BLOCK_SIZE, (x+1)*BLOCK_SIZE, (y+1)*BLOCK_SIZE, outline = 'black', fill = 'white',tag = 'grid')
def genPiece(board,p):
    keys = ['I','O','T', 'S', 'Z', 'J', 'L']
    return block.Piece(random.choice(keys),6,board)

def delRows(board):
    #make a rectangle for find overlapping for every row of the board
    #this will be run on a constant loop in timerFired
    #if the overlapping function returns a set of length of the a row
        #then, for every item in that row, delete from the board
        #all blocks on the board, except for the active piece will move down 1
        #its gonna be a fine all with tag
    pass
            
root = tk.Tk()
board = tk.Canvas(root, width = WIDTH, height = HEIGHT)
board.pack()
drawGrid(board)
#print(board.find_withtag('grid'))

#print(set(board.find_overlapping(1*(BLOCK_SIZE)+(BLOCK_SIZE/4),0*(BLOCK_SIZE)+(BLOCK_SIZE/4),1*(BLOCK_SIZE)+(BLOCK_SIZE-BLOCK_SIZE/4),0*(BLOCK_SIZE) + (BLOCK_SIZE-BLOCK_SIZE/4))) - set(board.find_withtag('blue')))

d = block.Block(0,0,'#551a8b',board)
c = block.Block(8,19,'red',board)
p = block.Piece('T', 6,board)
root.bind('<Key>',lambda event: keyPressed(event,p))
timerFired(board)
board.mainloop()
