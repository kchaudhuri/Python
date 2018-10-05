class Game():
    """docstring for ."""

    board = [[None,None,None],[None,None,None],[None,None,None]]

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

    def addToken(self,x,y,team):
        if team == "x":
            board[x][y] = "x"
        if team == "o":
            board[x][y] = "o"
