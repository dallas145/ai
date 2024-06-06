class Board:
    def __init__(self):
        self.c = 8
        self.r = 8
        self.m = [None] * self.c
        for i in range(self.r):
            self.m[i] = [None] * self.c
            for j in range(self.c):
                self.m[i][j] = "-"

    def __str__(self):
        b = []
        b.append('                    ') 
        b.append(' -------------------') 
        b.append('                    ') 
        b.append('   A B C D E F G H  ') 
        b.append(' -------------------') 
        for i in range(self.r):
            b.append(f'{8-i}| {" ".join(self.m[i])} |{8-i}')

        b.append(' -------------------') 
        b.append('   A B C D E F G H  ')
        return '\n'.join(b)
            
    
    def show(self):
        print(str(self))

        
Black = {"P": "pawn", "R": "rook", "K": "knight", "P": "pawn", }


def B_init(board):
    black = [["R", "N", "B", "K", "Q", "B", "N", "R"],\
             ["P", "P", "P", "P", "P", "P", "P", "P"]]

    white = [["r", "n", "b", "k", "q", "b", "n", "r"],\
             ["p", "p", "p", "p", "p", "p", "p", "p"]]

    for j in range(len(black)):
        for i in range(len(black[j])):
            board.m[j][i] = black[j][i]

    for j in range(len(white)):
        for i in range(len(white[j])):
            board.m[b.r - j - 1][i] = white[j][i]


def move(board, steps):
    try:
        step = steps.split()
        curP = step[0]
        curPx, curPy = ord(curP[0]) - 97, 7 - ( int(curP[1]) - 1 )
        nexP = step[1]
        nexPx, nexPy = ord(nexP[0]) - 97, 7 - ( int(nexP[1]) - 1 )
        if board.m[curPy][curPx] != "-":
            board.m[nexPy][nexPx] = board.m[curPy][curPx]
            board.m[curPy][curPx] = "-"
        else:
            raise Exception(f'There is nothing in {curP}')
    except Exception as error:
        print(error)
    board.show()
            

b = Board()
B_init(b)
b.show()

while True:
    step = input("Where to go? (xn xn) : ")
    move(b, step)