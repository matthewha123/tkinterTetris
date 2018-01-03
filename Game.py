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
            p.rotate('ccw',board)
        if(event.keysym == 'e'):
            p.rotate('cw',board)
#    if(event.keysym == 'Up'):
#        p.move('u',0,-1,board)
    
def timerFired(root,board):
    global p
    delay = 500
    if(lose(root,board,p)):
        message = 'GAME OVER'
        msg = tk.Message(root,text = message)
        msg.config(font = ('Comic Sans',40))
        msg.pack(side = 'top')
        return
    p.move('d',0,1,board)
    if(not p.active):
        p = genPiece(board,p)
    delRows(board,p)
    board.after(delay,timerFired,root,board)
def drawGrid(board):
    for x in range(WIDTH//BLOCK_SIZE):
        for y in range(HEIGHT//BLOCK_SIZE):
            board.create_rectangle(x*BLOCK_SIZE, y*BLOCK_SIZE, (x+1)*BLOCK_SIZE, (y+1)*BLOCK_SIZE, outline = 'black', fill = 'white',tag = 'grid')
def genPiece(board,p):
    keys = ['I','O','T', 'S', 'Z', 'J', 'L']
    return block.Piece(random.choice(keys),random.randint(0,6),board)

def delRows(board,p):
    for i in range(19,0,-1):
        olDel = set(board.find_overlapping(BLOCK_SIZE/4,BLOCK_SIZE*(i)+(BLOCK_SIZE/4),BLOCK_SIZE*9+(BLOCK_SIZE*(3/4)),BLOCK_SIZE*i + (BLOCK_SIZE *(3/4))))
        other = set(board.find_all()) - set(board.find_withtag('grid'))#- set(board.find_withtag('del'))
        if(len(olDel & other) == 10):
            for i in list(olDel & other):
                board.delete(i)
            for i in list(set(board.find_all()) - set(board.find_withtag('grid')) - set(p.blockIDs)):
                board.move(i,0,25)
def lose(root,board,p):
    olLose = set(board.find_overlapping(BLOCK_SIZE/4,(BLOCK_SIZE/4),BLOCK_SIZE*9+(BLOCK_SIZE*(3/4)),(BLOCK_SIZE *(3/4))))
    other = set(board.find_all()) - set(board.find_withtag('grid'))- set(p.blockIDs)
    if(olLose & other):
        return True
root = tk.Tk()
board = tk.Canvas(root, width = WIDTH, height = HEIGHT)
board.pack()
drawGrid(board)

p = block.Piece('I', 6,board)
root.bind('<Key>',lambda event: keyPressed(event,p))
timerFired(root,board)
board.mainloop()
