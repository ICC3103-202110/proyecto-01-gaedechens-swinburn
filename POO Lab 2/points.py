from gameboard import Gameboard
class Points(Gameboard):
    pointsp1= 0 #player 1 points
    pointsp2= 0 #player 2 points
    def __init__(self, pointsp1, pointsp2, pairs):
        #super(Points,self).__init__(pairs)
        self.pairs = pairs
        self.pointsp1 = Points.pointsp1
        self.pointsp2 = Points.pointsp2


   

