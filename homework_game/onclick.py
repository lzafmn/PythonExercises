try:
    from Tkinter import *
except:
    from tkinter import *

class grid_piece():

    def __init__(self, canvas, row, column, colour_boolean, size):
        colour_1 = '#934904'
        colour_2 = '#fce2c9'
        self.row = row
        self.column = column
        grid_piece = Button(canvas, height = size // 100,
                            width = size // 50,
                            command=lambda: my_board.button_press([row, column]))
        grid_piece.grid(row=row, column = column)
        if colour_boolean:
            grid_piece.configure(bg = colour_1, fg = colour_1)
        else:
            grid_piece.configure(bg = colour_2, fg = colour_2)

class pawn():

    def __init__(self, size, canvas, position):
        self.pawn_canvas = Canvas(canvas, width = size // 8, height = size // 8
                                  )
        self.pawn_canvas.grid(row = position[0], column = position[1])

class Board():

    def __init__(self, master, size):
        self.canvas = Canvas(master, width=size, height=size)
        self.canvas.pack()
        self.size = size

    def generate_board(self):
        colour_boolean = True
        self.board_array = []
        for column in range(8):
            column_pieces = []
            colour_boolean = not colour_boolean
            for row in range(8):
                colour_boolean = not colour_boolean
                piece = grid_piece(self.canvas, row, column, colour_boolean, self.size)
                column_pieces.append(piece)
            self.board_array.append(column_pieces)

    def display_pieces(self):
        white_pieces = []
        black_pieces = []       

        for x in range(8):
            Pawn = pawn(self.size, self.canvas, [1, x])
            white_pieces.append(Pawn)

    def button_press(self, position):
        print(position)

def onclick(*args):
    print(*args)       

root = Tk()

my_board = Board(root, 600)
my_board.generate_board()
my_board.display_pieces()

root.mainloop()
