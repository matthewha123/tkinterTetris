# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 13:19:43 2017

@author: matth
"""
BLOCK_SIZE = 25
import numpy as np

class Block(object):
    def __init__(self,x,y,color,board):
        self.b = board.create_rectangle(x*BLOCK_SIZE, y*BLOCK_SIZE, (x+1)*BLOCK_SIZE, (y+1)*BLOCK_SIZE, outline = 'black', fill = color,tag = 'block')
        self.x = x
        self.y = y
        self.pos = [self.x,self.y]
    def move(self,dr,board,piece):
        if(dr == 'r'):
            self.x += 1
            board.move(self.b,25,0)
        elif(dr == 'l'):
            self.x += -1
            board.move(self.b,-25,0)
        elif(dr == 'u'):
            self.y += -1
            board.move(self.b,0,-25)
        elif(dr == 'd'):
            self.y += 1
            board.move(self.b,0,25)    


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
        self.active = True
        for coord in (self.choices[choice][1:]):
            b = Block(coord[0]+sPos, coord[1]+sPos,self.choices[choice][0],board)
            self.blocks.append(b)
            self.blockIDs.append(b.b)
    def validMove(self,block,x,dx, y,dy, board, piece):
        #oL= set(board.find_overlapping((block.x+dx)*(BLOCK_SIZE)+(BLOCK_SIZE/4),(block.y+dy)*(BLOCK_SIZE)+(BLOCK_SIZE/4),(block.x+dx)*(BLOCK_SIZE)+(BLOCK_SIZE-BLOCK_SIZE/4),(block.y+dy)*(BLOCK_SIZE) + (BLOCK_SIZE-BLOCK_SIZE/4)))
        oL= set(board.find_overlapping((x+dx)*(BLOCK_SIZE)+(BLOCK_SIZE/4),(y+dy)*(BLOCK_SIZE)+(BLOCK_SIZE/4),(x+dx)*(BLOCK_SIZE)+(BLOCK_SIZE-BLOCK_SIZE/4),(y+dy)*(BLOCK_SIZE) + (BLOCK_SIZE-BLOCK_SIZE/4)))
        oLStop = set(board.find_overlapping((x)*(BLOCK_SIZE)+(BLOCK_SIZE/4),(y+dy)*(BLOCK_SIZE)+(BLOCK_SIZE/4),(x)*(BLOCK_SIZE)+(BLOCK_SIZE-BLOCK_SIZE/4),(y+dy)*(BLOCK_SIZE) + (BLOCK_SIZE-BLOCK_SIZE/4)))
        other = set(board.find_all()) - set(board.find_withtag('grid')) - set(piece.blockIDs)
        print(oL & other)
        if((x+dx)<0 or (x+dx) > 9 or (y+dy)<0 or (y+dy)>19):
            if(y+dy>18):
                self.active = False
            return False
        if(oL & other):
            if(oLStop & other):
                self.active = False
            return False
        else:
            return True
    def move(self,dr,dx,dy,board):
        for b in self.blocks:
            if(self.validMove(b,b.x,dx,b.y,dy,board,self)):
                continue
            else:
                return False
        for b in self.blocks:
            b.move(dr,board,self)
    def rotate(self, omega, board):
        rotM = 0
        if(omega == 'ccw'): rotM = np.matrix( ((0,-1),(1,0)) )
        else: rotM = np.matrix( ((0,1),(-1,0)) )
        newCoords = []
        for b in self.blockIDs:
            #subtract pivot coordinate from each coordiate pair
            pivotX = (board.coords(b)[0] / 25) - (board.coords(self.blockIDs[2])[0]/25)
            pivotY = (board.coords(b)[1] / 25) - (board.coords(self.blockIDs[2])[1]/25)
            
            #multiply coordinates by rotation matrix
            l = ((np.matrix((pivotX,pivotY)) * rotM) + np.matrix((board.coords(self.blockIDs[2])[0]/25,board.coords(self.blockIDs[2])[1]/25))).tolist()
            newCoords.append((l[0][0],l[0][1],l[0][0]+1,l[0][1]+1))
        
        #if valid coordinates pass!Need to add that check
        #pass in each new coordinate into validMove,using the x and y values as the dx and dy, x and y are 0
        for i in range(len(self.blockIDs)):
            board.coords(self.blockIDs[i],tuple([25*j for j in newCoords[i]]))
        #pivot piece is always the the third tuple in the piece dicitionary
        #subtract coordinates of pivot from every other piece
        #multiply by the rotation matrix
        #return coordinates of each piece as the new coordinates
        #check valid move with x and y as 0 and dx and dy as the new coordinates of every block
        
        #if they are valid moves then the for loop will complete with success
        #once this occurs, the new coordinates are set for the pieces.
        #these coordinates will have been stored in a dictionary for each of the pieces
        
        #counter clockwise matrix: [0,-1
        #                           1, 0]
        #clockwise matrix:         [0, 1
        #                           -1, 0]
        pass
    def genRotationCoordinates(self,omega):
        pass