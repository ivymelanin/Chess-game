import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (222, 184, 135)
DARK_BROWN = (139, 69, 19)
CHECK_COLOR = (255, 0, 0)

# Piece images
PIECES = {
    'r': pygame.image.load('images/black_rook.jfif'),
    'n': pygame.image.load('images/black_knight.jfif'),
    'b': pygame.image.load('images/black_bishop.jfif'),
    'q': pygame.image.load('images/black_queen.jfif'),
    'k': pygame.image.load('images/black_king.jfif'),
    'p': pygame.image.load('images/black_pawn.jfif'),
    'R': pygame.image.load('images/white_rook.jfif'),
    'N': pygame.image.load('images/white_knight.jfif'),
    'B': pygame.image.load('images/white_bishop.jfif'),
    'Q': pygame.image.load('images/white_queen.jfif'),
    'K': pygame.image.load('images/white_king.jfif'),
    'P': pygame.image.load('images/white_pawn.jfif'),
}

# Initial board setup
INITIAL_BOARD = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]

class ChessGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.clock = pygame.time.Clock()
        self.board = INITIAL_BOARD
        self.selected_piece = None
        self.current_turn = 'white'  # 'white' or 'black'
        self.check = False
        self.checkmate = False

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
                pygame.draw.rect(self.screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                piece = self.board[row][col]
                if piece != '.':
                    self.screen.blit(PIECES[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

    def select_piece(self, pos):
        x, y = pos
        col = x // SQUARE_SIZE
        row = y // SQUARE_SIZE
        if self.selected_piece:
            # Move the piece
            if self.is_valid_move(self.selected_piece, (col, row)):
                self.move_piece(self.selected_piece, (col, row))
                self.selected_piece = None
                self.current_turn = 'black' if self.current_turn == 'white' else '