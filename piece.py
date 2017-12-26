# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 14:07:35 2017

@author: matth
"""
import block
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
        for coord in (self.choices[choice][1:]):
            b = block.Block(coord[0]+sPos, coord[1]+sPos,self.choices[choice][0],board)
            self.blocks.append(b)
            
