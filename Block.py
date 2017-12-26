# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 13:19:43 2017

@author: matth
"""
BLOCK_SIZE = 25

class Block(object):
    def __init__(self,x,y,color,board):
        self.b = board.create_rectangle(x*BLOCK_SIZE, y*BLOCK_SIZE, (x+1)*BLOCK_SIZE, (y+1)*BLOCK_SIZE, outline = 'black', fill = color,tag = 'block')
        self.x = x
        self.y = y
        self.pos = [self.x,self.y]
    def move(self,dr,board,piece):
        if(dr == 'r'):
            if(validMove(self,self.x+1,self.y,board,piece)):
                self.x += 1
                board.move(self.b,25,0)
            else:
                print('fuck')
        elif(dr == 'l'):
            if(validMove(self,self.x-1,self.y,board,piece)):
                self.x += -1
                board.move(self.b,-25,0)
        elif(dr == 'u'):
            if(validMove(self,self.x,self.y-1,board,piece)):
                self.y += -1
                board.move(self.b,0,-25)
        elif(dr == 'd'):
            if(validMove(self,self.x,self.y+1,board,piece)):
                self.y += 1
                board.move(self.b,0,25)    
#have to change it so that move is looped through elsewhere, like here
def validMove(block,dx, dy, board, piece):
    #oL= set(board.find_overlapping((block.x+dx)*(BLOCK_SIZE)+(BLOCK_SIZE/4),(block.y+dy)*(BLOCK_SIZE)+(BLOCK_SIZE/4),(block.x+dx)*(BLOCK_SIZE)+(BLOCK_SIZE-BLOCK_SIZE/4),(block.y+dy)*(BLOCK_SIZE) + (BLOCK_SIZE-BLOCK_SIZE/4)))
    oL= set(board.find_overlapping((dx)*(BLOCK_SIZE)+(BLOCK_SIZE/4),(dy)*(BLOCK_SIZE)+(BLOCK_SIZE/4),(dx)*(BLOCK_SIZE)+(BLOCK_SIZE-BLOCK_SIZE/4),(dy)*(BLOCK_SIZE) + (BLOCK_SIZE-BLOCK_SIZE/4)))
    other = set(board.find_all()) - set(board.find_withtag('grid')) - set(piece.blockIDs)
    print(oL & other)
    if(oL & other):
        return False
    else:
        return True

class Piece(object):
    choices = {'I':('cyan',(0,0),(1,0),(2,0),(3,0)),
               'O':('yellow',(0,0),(1,0),(0,1),(1,1)),
               'T':('#551a8b',(1,0),(0,1),(1,1),(2,1)),
                'S':('green',(1,0),(0,1),(1,1),(2,0)),
                'Z':('red',(0,0),(1,0),(1,1),(1,2)), 
                'J':('blue',(0,0),(0,1),(1,1),(1,2)),
                'L':('#ffa500',(0,1),(1,1),(2,1),(2,0))}
    def __init__(self,choice,sPos,board):
        self.blocks = []
        self.blockIDs = []
        for coord in (self.choices[choice][1:]):
            b = Block(coord[0]+sPos, coord[1]+sPos,self.choices[choice][0],board)
            self.blocks.append(b)
            self.blockIDs.append(b.b)