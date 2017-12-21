import Board

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