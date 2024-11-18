from pieces.piece import piece
import math

class pawn(piece):

    alliance = None
    position= None
    enpassant=False

    def __init__(self,alliance,position):
        self.alliance=alliance
        self.position=position


    def tostring(self):
        return 'P' if self.alliance == "Black" else "p"

    def calculatecoordinates(self):
        a=self.position/8
        b=self.position%8
        return[math.floor(a),b]


    def legalmoveb(self,gametiles):
        legalmoves=[]
        x=self.calculatecoordinates()[0]
        y=self.calculatecoordinates()[1]
        if(gametiles[x][y].pieceonTile.alliance=='Black'):

            if(x==1):
                if(gametiles[x+1][y].pieceonTile.tostring()=='-' ):
                    legalmoves.append([x+1,y])
                    if(gametiles[x+2][y].pieceonTile.tostring()=='-'):
                        legalmoves.append([x+2,y])
                if(y+1>7):
                    if(gametiles[x+1][y-1].pieceonTile.alliance=='White'):
                        legalmoves.append([x+1,y-1])
                if(y-1<0):
                    if(gametiles[x+1][y+1].pieceonTile.alliance=='White'):
                        legalmoves.append([x+1,y+1])
                if(y+1<8 and y-1>=0):
                    if(gametiles[x+1][y-1].pieceonTile.alliance=='White'):
                        legalmoves.append([x+1,y-1])
                    if(gametiles[x+1][y+1].pieceonTile.alliance=='White'):
                        legalmoves.append([x+1,y+1])
                return legalmoves



            else:
                if(gametiles[x+1][y].pieceonTile.tostring()=='-'  ):
                    legalmoves.append([x+1,y])
                if(y+1>7):
                    if(gametiles[x+1][y-1].pieceonTile.alliance=='White'):
                        legalmoves.append([x+1,y-1])
                if(y-1<0):
                    if(gametiles[x+1][y+1].pieceonTile.alliance=='White'):
                        legalmoves.append([x+1,y+1])
                if(y+1<8 and y-1>=0):
                    if(gametiles[x+1][y-1].pieceonTile.alliance=='White'):
                        legalmoves.append([x+1,y-1])
                    if(gametiles[x+1][y+1].pieceonTile.alliance=='White'):
                        legalmoves.append([x+1,y+1])

                return legalmoves


        if(gametiles[x][y].pieceonTile.alliance=='White'):

            if(x==6):
                if(gametiles[x-1][y].pieceonTile.tostring()=='-' ):
                    legalmoves.append([x-1,y])
                    if(gametiles[x-2][y].pieceonTile.tostring()=='-'):
                        legalmoves.append([x-2,y])
                if(y+1>7):
                    if(gametiles[x-1][y-1].pieceonTile.alliance=='Black'):
                        legalmoves.append([x-1,y-1])
                if(y-1<0):
                    if(gametiles[x-1][y+1].pieceonTile.alliance=='Black'):
                        legalmoves.append([x-1,y+1])
                if(y+1<8 and y-1>=0):
                    if(gametiles[x-1][y-1].pieceonTile.alliance=='Black'):
                        legalmoves.append([x-1,y-1])
                    if(gametiles[x-1][y+1].pieceonTile.alliance=='Black'):
                        legalmoves.append([x-1,y+1])
                return legalmoves



            else:
                if(gametiles[x-1][y].pieceonTile.tostring()=='-'  ):
                    legalmoves.append([x-1,y])
                if(y+1>7):
                    if(gametiles[x-1][y-1].pieceonTile.alliance=='Black'):
                        legalmoves.append([x-1,y-1])
                if(y-1<0):
                    if(gametiles[x-1][y+1].pieceonTile.alliance=='Black'):
                        legalmoves.append([x-1,y+1])
                if(y+1<8 and y-1>=0):
                    if(gametiles[x-1][y-1].pieceonTile.alliance=='Black'):
                        legalmoves.append([x-1,y-1])
                    if(gametiles[x-1][y+1].pieceonTile.alliance=='Black'):
                        legalmoves.append([x-1,y+1])

                return legalmoves